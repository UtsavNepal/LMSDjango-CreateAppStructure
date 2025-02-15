from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'Name', 'Email', 'ContactNumber', 'Department']
    search_fields = ['Name', 'Email']
    list_filter = ['Department']
    ordering = ['Name']

admin.site.register(Student, StudentAdmin)
