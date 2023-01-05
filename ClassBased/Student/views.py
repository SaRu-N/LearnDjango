from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView, RedirectView
from django.views import View
from .forms import StudentRegistration
from .models import Student
# Create your views here.
class AddStudentView(TemplateView):
    template_name ='student/add.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        fm=StudentRegistration()
        context= {'form':fm}
        return context
    def post(self,request):
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('../../student/details')
class HomeView(TemplateView):
    template_name='student/home.html'
class ProfileView(TemplateView):
    template_name='student/profile.html'
class ShowStudentView(TemplateView):
    template_name='student/show.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        stud= Student.objects.all()
        context={'stud':stud}
        return context
class SignUpView(TemplateView):
    template_name='student/signup.html'
class LoginView(TemplateView):
    template_name='student/login.html'
class UpdateStudentView(View):
    template_name='student/update.html'
    def get(self,request,id):
        st=Student.objects.get(pk=id)
        fm=StudentRegistration(instance=st)
        return render(request, 'student/update.html',{'form':fm})
    def post(self,request,id):
        st=Student.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=st)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('../../details')


class LogOutView(TemplateView):
    pass
class DeleteStudentView(RedirectView):
    url='/student/details/'
    def get_redirect_url(self, *args, **kwargs):
        del_id=kwargs['id']
        Student.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)


