from django.contrib import admin

from market.models import Books


# Register your models here.
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['name', 'page_count', 'category', 'author_name', 'image']
    search_fields = ['name', 'author_name']