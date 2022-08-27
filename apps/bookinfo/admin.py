from django.contrib import admin
from .models import *

class BookInfoImageInline(admin.TabularInline):
    model = BookImage
    extra = 1


class RateInline(admin.TabularInline):
    model = Rate
    extra = 1


class BookInfoAdmin(admin.ModelAdmin):
    inlines = [BookInfoImageInline, RateInline]
    list_display = ['id', 'name', 'is_deleted']


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Rate)
admin.site.register(BookInfo, BookInfoAdmin)
