from django.urls import path
from .views import DashboardView, GetOverdueBorrowersView, MailOverdueBorrowersView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('dashboard/GetOverdueBorrowers', GetOverdueBorrowersView.as_view(), name='overdue-borrowers'),
    path('dashboard/MailOverdueBorrowers', MailOverdueBorrowersView.as_view(), name='mail-overdue-borrowers'),
]
