# Generated by Django 3.2.7 on 2021-09-08 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=20)),
                ('password', models.IntegerField(max_length=8)),
                ('confirmpass', models.IntegerField(max_length=8)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]
