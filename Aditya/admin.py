from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "sort_order")
    list_editable = ("sort_order",)
    search_fields = ("title", "category", "description")
