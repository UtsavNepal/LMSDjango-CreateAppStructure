# Generated by Django 5.1.4 on 2025-02-15 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='BookId',
            new_name='book_id',
        ),
    ]
