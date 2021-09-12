from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100,null=True)
    Email = models.EmailField(max_length=20,null=True)
    password = models.IntegerField(max_length=8,null=True)
    confirm_password = models.IntegerField(max_length=8,null=True)
    city = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

