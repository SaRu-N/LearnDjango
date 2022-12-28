from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    # creator=models.ForeignKey(User,on_delete=models.CASCADE)
    creator=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    blog_name =models.CharField(max_length=70)
    blog_cat =models.CharField(max_length=70)
    blog_pdate =models.DateField()

class Like(Blog):
    pag=models.OneToOneField(Blog,on_delete=models.CASCADE,primary_key=True,parent_link=True)
    likes = models.IntegerField()
