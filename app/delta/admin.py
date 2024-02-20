
from projects.models import ProjectElement
from django.contrib import admin

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['ref', 'project_name', 'product', 'qty', 'total_lm', 'weight']
    search_fields = ['ref', 'project_name', 'product']
    readonly_fields = ['total_lm', 'total_m2', 'total_lm_1', 'total_m2_1']


admin.site.register(ProjectElement, ProjectAdmin)