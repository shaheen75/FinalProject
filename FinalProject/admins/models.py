from django.db import models

# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_img = models.CharField(max_length=100)
    book_details = models.CharField(null=True,max_length=10000)
    return_date = models.DateField(null=True)
    borrowed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_name

