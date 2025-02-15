from django.contrib import admin
from .models import Transaction

@admin.action(description="Mark selected transactions as Returned")
def mark_as_returned(modeladmin, request, queryset):
    queryset.update(transaction_type='returned')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'student_id', 'book_id', 'transaction_type', 'date_of_borrowed', 'due_date', 'user_id')
    search_fields = ('student__name', 'book__title', 'transaction_type')
    list_filter = ('transaction_type',)
    ordering = ['date_of_borrowed']
    actions = [mark_as_returned]
