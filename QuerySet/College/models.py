from django.db import models

# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=100,null=False)
    roll = models.IntegerField(unique=True,null=False)
    address= models.CharField(max_length=100)
    dob = models.DateField()
    marks = models.IntegerField()
    passed_date=models.DateField()
class Teacher(models.Model):
    name= models.CharField(max_length=100,null=False)
    code = models.IntegerField(unique=True,null=False)
    address= models.CharField(max_length=100)
    join_date = models.DateField()
    salary = models.IntegerField()