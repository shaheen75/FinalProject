# Generated by Django 3.2.7 on 2021-09-12 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('book_author', models.CharField(max_length=100)),
                ('book_img', models.CharField(max_length=100)),
                ('book_details', models.CharField(max_length=100)),
                ('return_date', models.DateField(null=True)),
                ('borrowed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
