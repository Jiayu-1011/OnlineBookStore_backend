from django.db import models

# Create your models here.

class Member(models.Model):
    account = models.CharField(max_length=64, primary_key=True)
    password = models.CharField(max_length=64)
    name = models.CharField(max_length=64)


class Book(models.Model):
    bookId = models.CharField(max_length=64, primary_key=True)
    name = models.CharField(max_length=64)
    price = models.FloatField(max_length=64)



