# Generated by Django 3.2.7 on 2021-09-16 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0002_alter_book_book_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]