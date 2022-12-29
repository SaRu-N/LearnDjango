from django.contrib import admin
from . models import Page,Post,Song
# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display=['page_name','page_cat','page_pdate','user']
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','post_title','post_cat','post_pdate','user']
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display=['id','song_name','song_duration','sang_by']