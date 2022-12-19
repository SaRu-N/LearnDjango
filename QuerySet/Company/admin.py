from django.contrib import admin
from .models import Customer,Employee
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','csid','name','email','phone','address']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','empid','name','salary','phone','address']