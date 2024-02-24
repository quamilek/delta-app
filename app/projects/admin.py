from django.contrib import admin
from projects.models import Client, Project, ProjectElement

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name'] 


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'client'] 
    search_fields = ['name', 'client'] 


@admin.register(ProjectElement)
class ProjectElementAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'ref', 'description', 'qty_1'] 
    search_fields = ['project', 'client'] 