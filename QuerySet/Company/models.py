from django.db import models

# Create your models here.
class Customer(models.Model):
    name= models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    address=models.CharField(max_length=200)
    csid=models.IntegerField(unique=True)

class Employee(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    salary=models.IntegerField()
    address=models.CharField(max_length=200)
    empid=models.IntegerField(unique=True)
