from django.contrib import admin
from .models import Post 
@admin.register(Post) 

class PostAdmin(admin.ModelAdmin): 
    list_display = ("title", "language", "category", "is_published", "created_at") 
    list_filter = ("language", "category", "is_published") 
    prepopulated_fields = {"slug": ("title",)}