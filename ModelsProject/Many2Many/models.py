from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Song(models.Model):
    singer =models.ManyToManyField(User)
    sname=models.CharField(max_length=100)
    sdur=models.IntegerField()

    def song_by(self):
        return ",".join([str(p) for p in self.singer.all()])