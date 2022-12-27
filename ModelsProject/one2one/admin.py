from django.contrib import admin
from . models import Page, Like
# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display=['page_name','page_cat','page_pdate','user']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display=['page_name','like','page_pdate','user']