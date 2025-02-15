from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['book_id', 'Title', 'Author', 'Genre', 'ISBN', 'Quantity'] 
    search_fields = ['Title', 'ISBN'] 
    list_filter = ['Genre', 'Author']  
    ordering = ['Title'] 
    
    raw_id_fields = ['Author'] 

admin.site.register(Book, BookAdmin)





