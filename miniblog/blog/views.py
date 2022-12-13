from django.shortcuts import render, HttpResponseRedirect
from . forms import SignUpForm, LogInForm, AddPostForm
from django.contrib.auth import authenticate, login, logout
from . models import Post
from django.contrib.auth.models import Group
# Create your views here.
def homePage(request):
    posts =Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})

def aboutPage(request):
    return render(request,'blog/about.html')

def contactPage(request):
    return render(request,'blog/contact.html')
    
def dashboard(request):
    if request.user.is_authenticated:
        posts= Post.objects.all()
        user=request.user
        full_name=user.get_full_name()
        grps =user.groups.all()
        return render(request,'blog/dashboard.html',{'posts':posts,'fullname':full_name,'groups':grps})
    else:
        return HttpResponseRedirect('../signup')

def loginPage(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            fm= LogInForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user= authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('../dashboard/')
                
        else:
            fm=LogInForm()
    else:
        return HttpResponseRedirect('../dashboard')

    return render(request,'blog/login.html',{'form':fm})

def signupPage(request):
    if request.method == 'POST':
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            user=fm.save()
            group= Group.objects.get(name='Author')
            user.groups.add(group)
            return HttpResponseRedirect('../login')
    else:
        fm=SignUpForm()
    return render(request,'blog/signup.html',{'form':fm})

def logoutPage(request):
 if request.user.is_authenticated:
    logout(request)
 return HttpResponseRedirect('../home')

def addPost(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=AddPostForm(request.POST)
            if fm.is_valid():
                title = fm.cleaned_data['title']
                description = fm.cleaned_data['description']
                post=Post(title=title,description=description)
                post.save()
                return HttpResponseRedirect('../../dashboard')

        else:
            fm=AddPostForm()
        return render(request,'blog/addpost.html',{'form':fm})
    else:
        return HttpResponseRedirect('../login')
def editPost(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pst=Post.objects.get(pk=id)
            fm=AddPostForm(request.POST,instance=pst)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('../../dashboard')
        else:
            pst=Post.objects.get(pk=id)
            fm=AddPostForm(instance=pst)
        return render(request, 'blog/editpost.html',{'form':fm})

    else:
        return HttpResponseRedirect('../login')
       
def deletePost(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pst=Post.objects.get(pk=id)
            pst.delete()
            return HttpResponseRedirect('../../dashboard')
        else:
            return HttpResponseRedirect('../../login')