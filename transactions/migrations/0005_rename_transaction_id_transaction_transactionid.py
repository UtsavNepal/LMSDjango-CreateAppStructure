# Generated by Django 5.1.4 on 2025-02-15 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_remove_transaction_user_id_transaction_userid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='transaction_id',
            new_name='TransactionId',
        ),
    ]
