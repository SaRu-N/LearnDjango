from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Phone=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    Faculty=models.CharField(max_length=50)
