from django.shortcuts import render
from . models import Page, Post,Song,User
# Create your views here.

def home(request):
    return render(request,'myapp/home.html')
def ShowUser(request):
    data1=User.objects.all()
    return render(request, 'myapp/user.html',{'user':data1})
def ShowPage(request):
    data1=Page.objects.all()
    return render(request, 'myapp/page.html',{'page':data1})
def ShowPost(request):
    data1=Post.objects.all()
    return render(request, 'myapp/post.html',{'post':data1})
def ShowSong(request):
    data1=Song.objects.all()
    return render(request, 'myapp/song.html',{'song':data1})