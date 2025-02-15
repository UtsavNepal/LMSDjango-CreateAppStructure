from .models import Transaction

class TransactionRepository:
    @staticmethod
    def get_all_transactions():
        return Transaction.objects.all()

    @staticmethod
    def get_transaction_by_id(transaction_id):
        return Transaction.objects.filter(transaction_id=transaction_id).first()

    @staticmethod
    def create_transaction(data):
        return Transaction.objects.create(**data)

    @staticmethod
    def update_transaction(transaction_id, data):
        transaction = Transaction.objects.filter(transaction_id=transaction_id).first()
        if transaction:
            for key, value in data.items():
                setattr(transaction, key, value)
            transaction.save()
        return transaction

    @staticmethod
    def delete_transaction(transaction_id):
        return Transaction.objects.filter(transaction_id=transaction_id).delete()
