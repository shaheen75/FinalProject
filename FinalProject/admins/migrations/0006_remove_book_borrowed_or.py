# Generated by Django 3.2.7 on 2021-09-19 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0005_book_borrowed_or'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='borrowed_or',
        ),
    ]
