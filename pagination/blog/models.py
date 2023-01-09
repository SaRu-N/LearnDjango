from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    post_title =models.CharField(max_length=70)
    post_cat = models.CharField(max_length=70)
    post_desc = models.CharField(max_length=600)
    post_pdate=models.DateField()
