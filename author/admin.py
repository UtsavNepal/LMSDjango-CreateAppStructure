from django.contrib import admin
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['AuthorId', 'Author_Name', 'Bio'] 
    search_fields = ['Author_Name']  
    list_filter = ['Author_Name']  
    ordering = ['Author_Name']  

admin.site.register(Author, AuthorAdmin)
