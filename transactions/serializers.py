
from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def validate(self, data):
        # Check if the same student has already borrowed the same book
        if Transaction.objects.filter(StudentId=data['StudentId'], BookId=data['BookId'], TransactionType='borrowed').exists():
            raise serializers.ValidationError(f"Student {data['StudentId'].Name} has already borrowed the book {data['BookId'].Title}.")
        return data
