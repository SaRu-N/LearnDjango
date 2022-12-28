from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import Blog, Like
# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=['blog_name','blog_cat','blog_pdate','creator']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display=['blog_name','like','blog_pdate','creator']