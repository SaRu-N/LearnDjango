from django.db import models
from django.urls import reverse

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField()
    password=models.CharField(max_length=10)


    # def get_absolute_url(self):
    #     return reverse('thankyou')

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})