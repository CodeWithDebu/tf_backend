# from django.shortcuts import render

# # import view sets from the REST framework
# from rest_framework import viewsets

# # import the TodoSerializer from the serializer file
# from .serializers import TodoSerializer

# # import the Todo model from the models file
# from .models import Todo

# # create a class for the Todo model viewsets
# class TodoView(viewsets.ModelViewSet):

# 	# create a serializer class and 
# 	# assign it to the TodoSerializer class
# 	serializer_class = TodoSerializer

# 	# define a variable and populate it 
# 	# with the Todo list objects
# 	queryset = Todo.objects.all()

import csv
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer
from openpyxl import Workbook
from rest_framework import viewsets


# Existing TodoView class for CRUD operations
class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

# New view to export data as CSV
class ExportCsv(View):
    def get(self, request, *args, **kwargs):
        todos = Todo.objects.all()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="todos.csv"'
        writer = csv.writer(response)
        writer.writerow(['Title', 'Description', 'Completed'])
        for todo in todos:
            writer.writerow([todo.title, todo.description, todo.completed])
        return response

# New view to export data as Excel
class ExportExcel(View):
    def get(self, request, *args, **kwargs):
        todos = Todo.objects.all()
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="todos.xlsx"'
        wb = Workbook()
        ws = wb.active
        ws.append(['Title', 'Description', 'Completed'])
        for todo in todos:
            ws.append([todo.title, todo.description, todo.completed])
        wb.save(response)
        return response

