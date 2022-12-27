from django.db import models

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('name')
    def get_emp_range(self,r1,r2):
        return super().get_queryset().filter(empid__range=(r1,r2))