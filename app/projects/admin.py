from django.contrib import admin
from projects.models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name']  # Customize the fields displayed in the admin list
    search_fields = ['name'] 