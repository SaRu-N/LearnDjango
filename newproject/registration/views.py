from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
# Create your views here.
@login_required
def profile(request):
    return render(request,'registration/profile.html')

@staff_member_required
def about(request):
    return render(request,'registration/about.html')
@permission_required('registration.can_add_user')
def contact(request):
    return render(request,'registration/contact.html')
#### Class Based Views for decorationg in urls.py
# class ProfileView(TemplateView):
#     template_name='registration/profile.html'
#     def get_context_data(self, **kwargs):
#         context= super().get_context_data(**kwargs)
#         context['view_type']='Class Based'
#         return context
# class AboutView(TemplateView):
#     template_name='registration/about.html'
#     def get_context_data(self, **kwargs):
#         context= super().get_context_data(**kwargs)
#         context['view_type']='Class Based'
#         return context
# class ContactView(TemplateView):
#     template_name='registration/contact.html'
#     def get_context_data(self, **kwargs):
#         context= super().get_context_data(**kwargs)
#         context['view_type']='Class Based'
#         return context

#### Class Based Views
class ProfileView(TemplateView):
    template_name='registration/profile.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['view_type']='Class Based'
        return context
@method_decorator(staff_member_required,name='dispatch')
class AboutView(TemplateView):
    template_name='registration/about.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['view_type']='Class Based'
        return context

@method_decorator(permission_required('registration.can_add_user'),name='dispatch')
class ContactView(TemplateView):
    template_name='registration/contact.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['view_type']='Class Based'
        return context