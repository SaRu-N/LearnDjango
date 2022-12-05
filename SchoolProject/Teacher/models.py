from django.db import models

# Create your models here.
class Teacher(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Phone=models.CharField(max_length=10)
    Password=models.CharField(max_length=20,default='12345')