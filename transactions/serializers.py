from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def validate(self, data):
       
        transaction_instance = getattr(self, 'instance', None)

      
        if not transaction_instance:
           
            if Transaction.objects.filter(student_id=data['student_id'], book_id=data['book_id'], transaction_type='borrowed').exists():
                raise serializers.ValidationError(f"Student {data['student_id'].Name} has already borrowed the book {data['book_id'].Title}.")
        else:
          
            if data.get('transaction_type') == 'borrowed' and transaction_instance.transaction_type != 'borrowed':
                if Transaction.objects.filter(student_id=data['student_id'], book_id=data['book_id'], transaction_type='borrowed').exists():
                    raise serializers.ValidationError(f"Student {data['student_id'].Name} has already borrowed the book {data['book_id'].Title}.")
        
        return data
