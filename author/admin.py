from django.contrib import admin
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['AuthorId', 'Name', 'Bio'] 
    search_fields = ['Name']  
    list_filter = ['Name']  
    ordering = ['Name']  

admin.site.register(Author, AuthorAdmin)
