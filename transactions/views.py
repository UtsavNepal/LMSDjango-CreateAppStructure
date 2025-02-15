from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @action(detail=True, methods=['put'])
    def return_book(self, request, pk=None):
        transaction = self.get_object()
        if transaction.TransactionType == 'returned':
            raise ValidationError("This book has already been returned.")

        transaction.TransactionType = 'returned'
        transaction.save()
        return Response({'status': 'book returned'})

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValueError as e:
            raise ValidationError(str(e))
        
    permission_classes = [AllowAny]

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [AllowAny]

class TransactionRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [AllowAny]