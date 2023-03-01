from django.contrib import admin
from .models import PostModel, CategoryModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    "Class for registration BlogpostCategory model"
    list_display = ["pk", "title"]


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    "Class for registration BlogpostModel model"
    list_display = ["pk", "name", "category", "created_at", "updated_at"]
