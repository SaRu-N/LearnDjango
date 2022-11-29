from django.db import models

# Create your models here.
class Student(models.Model):
    stuid=models.IntegerField()
    stuname=models.CharField(max_length=100)
    stuemail=models.EmailField()
    stupass=models.CharField(max_length=10)
    comment=models.CharField(max_length=50,default='not availabe ')
