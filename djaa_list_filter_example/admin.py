from django.contrib import admin

from djaa_list_filter.admin import (
    AjaxAutocompleteListFilterModelAdmin,
)

from .models import Category, Post, Tag


@admin.register(Post)
class PostAdmin(AjaxAutocompleteListFilterModelAdmin):
    list_display = ('__str__', 'author', 'show_tags')
    autocomplete_list_filter = ('category', 'author', 'tags')

    def show_tags(self, obj):
        return ' , '.join(obj.tags.values_list('name', flat=True))


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    ordering = ['title']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['name']
