from django.contrib import admin

from .models import Student

# Register your models here.
@admin.register(Student)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
