# Generated by Django 5.1.6 on 2025-02-15 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserSignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('librarian', 'Librarian')], default='librarian', max_length=10)),
                ('access_token', models.CharField(editable=False, max_length=32, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
