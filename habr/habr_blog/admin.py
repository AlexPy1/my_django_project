from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class HabrBlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','time_create','username', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'cat', 'content', 'photo','get_html_photo','username', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}

# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'username', 'email')
#     list_display_links = ('id', 'username')
#     search_fields = ('username',)
#     prepopulated_fields = {'slug': ('username',)}
#     readonly_fields = ('last_login', 'date_joined',)

admin.site.register(Post, HabrBlogAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(CustomUser, CustomUserAdmin)

admin.site.site_title = 'Админ-панель'
admin.site.site_header = 'Админ-панель'