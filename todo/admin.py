# from django.contrib import admin

# # import the model Todo
# from .models import Todo

# # create a class for the admin-model integration
# class TodoAdmin(admin.ModelAdmin):

# 	# add the fields of the model here
# 	list_display = ("title","description","completed")

# # we will need to register the
# # model class and the Admin model class
# # using the register() method
# # of admin.site class
# admin.site.register(Todo,TodoAdmin)

from django.contrib import admin
from django.http import HttpResponse
import csv

from .models import Todo

# Custom admin action to export selected todos to CSV
def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="todos.csv"'
    writer = csv.writer(response)
    writer.writerow(['Title', 'Description', 'Completed'])
    for todo in queryset:
        writer.writerow([todo.title, todo.description, todo.completed])
    return response

export_to_csv.short_description = 'Export selected todos to CSV'

# Customizing the Todo admin view
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')
    actions = [export_to_csv]  # Add the export action to the admin view

# Register the Todo model with the custom admin view
admin.site.register(Todo, TodoAdmin)
