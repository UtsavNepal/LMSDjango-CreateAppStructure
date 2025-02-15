# transactions/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionListCreateView, TransactionRetrieveUpdateDeleteView, TransactionViewSet

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionRetrieveUpdateDeleteView.as_view(), name='transaction-detail'),
]
