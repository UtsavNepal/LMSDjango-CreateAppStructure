import logging
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

logger = logging.getLogger('transaction_logger')

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [AllowAny]

    @action(detail=True, methods=['put'])
    def return_book(self, request, pk=None):
        # Log the attempted URL
        logger.info(f"Attempted URL: {request.path}")

        transaction = self.get_object()
        if transaction.TransactionType == 'returned':
            logger.warning(f"Attempt to return already returned book: {transaction.id}")
            raise ValidationError("This book has already been returned.")

        transaction.TransactionType = 'returned'
        transaction.save()
        logger.info(f"Book {transaction.book_id} returned by user {transaction.user_id}")
        return Response({'status': 'book returned'})

    def create(self, request, *args, **kwargs):
        # Log the attempted URL
        logger.info(f"Attempted URL: {request.path}")
        
        try:
            response = super().create(request, *args, **kwargs)
            logger.info(f"Transaction created: {response.data}")
            return response
        except ValueError as e:
            logger.error(f"Transaction creation failed: {e}", exc_info=True)
            raise ValidationError(str(e))

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # Log the attempted URL
        logger.info(f"Attempted URL: {request.path}")
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Log the attempted URL
        logger.info(f"Attempted URL: {request.path}")
        return super().post(request, *args, **kwargs)

class TransactionRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        
        logger.info(f"Attempted URL: {request.path}")
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        
        logger.info(f"Attempted URL: {request.path}")
        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        
        logger.info(f"Attempted URL: {request.path}")
        return super().delete(request, *args, **kwargs)
