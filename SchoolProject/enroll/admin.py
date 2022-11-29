from django.contrib import admin
from enroll.models import Student
# Register your models here.
# using decorator
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display= ('id','stuid','stuname','stuemail','stupass')
#no need of below code while using decorator
#  admin.site.register(Student,StudentAdmin)
