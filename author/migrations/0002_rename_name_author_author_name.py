# Generated by Django 5.1.6 on 2025-02-16 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='Name',
            new_name='Author_Name',
        ),
    ]
