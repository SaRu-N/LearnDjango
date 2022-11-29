from django.db import models

# Create your models here.
class Student(models.Model):
    stuid=models.IntegerField()
    stuname=models.CharField(max_length=100)
    stuemail=models.EmailField()
    stupass=models.CharField(max_length=10)
    comment=models.CharField(max_length=50,default='not available')
    def __str__(self):
        # return self.stuname
        # we must convert int to string while using __str__ method
        return str(self.stuid)
