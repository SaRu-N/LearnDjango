#### Create virtual Environment
conda create --name anyname
#### To activate virtual Environment
conda activate anyname //djnago3
#### To deactivate Virtual Environment
conda deactivate

# Steps to work in django project 

>- create project
>
>- create app
>
>- add/install app in project
>
>- create templates folder in root directory or create templates folder inside every application
>
>- create folder having same name as app
>
>- add files
>
>- create separate for each applications inside templates (if common templates folder is used)
>
>- add templates directory in settings.py
>
>- create static folder in root project folder
>
>- create static files inside their respective folders in static
>
>- add static directory in settings.py
>
>- create model class and implement them
>
>- create a view
>
>- add url path of view:
>
>- inside application and register in innerProject (if separate urls.py is used for each application)
>
>

### Create new project
django-admin startproject ProjectName
### Create new application
-->ProjectName
python manage.py startapp AppName

### Installing application in project
-->settings.py-->INSTALLED_APPS:add appication name
### creating views in function based
-->AppName-->views.py:: def function_name(request):
                            return HttpResponse(html/variable/text)
from django.http import HttpResponse

### Create Model Class

inside application folder-->models.py

syntax: 

`class ClassName(models.Model):`

​	`field_name=models.FieldType(arg,options)`

##### Use Model class

- open settings.py
- register the application
- in terminal run `python manage.py makemigrations` and `python manage.py migrate`

##### writing code to get db data in views.py

- import model class from models.py

- inside function use all() method a

  `anyname=ModelClassName.objects.all()`

##### register model

- open admin.py file inside application folder
- import model class 
- `admin.site.register(ModelClassName)`
- 

#### Create Django Form using Form Class

- inside application create a file forms.py

- -->forms.py create form class using

  `from django import forms`

  `class FormClassName(forms.Form):`

  ​	`label=froms.FieldType()`

  ​	`label froms.FieldType(label='display_label')`

###### Display Form to user

-  create an form object inside view.py 
- pass that object to template file as a dict.
- `form .forms import FormClass`

##### Saving data in database using django form api

- create model class and make related form
- register model class in admins.py
- 

#### Rendering Templates Files

views.py:: from django.shortcuts import render

def function_name(request):

​	return render(request,'template_name',context=dict_name,content_type=MIME_type, status=None, using=None)

### Define url name for view
###### Using urls.py of innerproject
from app import views
-->innerProject-->urls.py-->URL_PATTERNS: add path('route/',views_path)
path(route,views,kwargs=None,name=None)

If views from multiple application are used any of below methods can be used:
1.from app import views as anyname

2. from app.views import function_name

###### using urls.py inside application
syntax for include():
include(module,namespace=None) or include(pattern_list) or include((pattern_list, app_namespace),namespace=None)

>create urls.py file in application
>write all url pattern in urls.py file
>include applications urls.py file in urls.py of innerProject
---

### Adding Template directory

-->settings.py::: create variable TEMPLATES_DIR= [BASE_DIR / 'templates']

find list TEMPLATES[

'DIRS':[TEMPLATES_DIR]

]

can directly write "[BASE_DIR / 'templates']" in 'DIRS'

### Adding Static directory

-->settings.py::: find list STATIC_URL  and Add STATICFILES_DIRS= [BASE_DIR / 'static']

#### using static files in templates

> first load static files     {%load static%} in the beginning
>
> reference static files <link href='{%static "filepath"%}'>  whenever needed

#### Create Hyberlink using url tag

without using url tag

> `<a href="/anyname">AnyName</a>`
>
> can use dynamic href value
>
> `<a href="{{an}}">AnyName</a>` 
>
> where `an` must come from function as:
>
> `def anyname(request):`
>
> `return render(request,'html',{'an':'/anyname})`

using url tag

> provide value for Name argument in path()
>
> use same name in url tag to create hyperlink
>
> ​	`<a href="{%url'urlname' %}">AnyName</a>`
>
> 

##### Get Django form data in terminal

inside views.py

example

def formdata(request):

​	if request.method=='POST':

​		fm=FormClassName(request.POST)

​		if fm.is_valid():

​			print("form validated")

​			print("anyname",fm.cleaned_data['fieldname'])

​	else:

​		fm=FormClassName()

​	return render(request,'templatepath','dict')

### STRUCTURE OF DJANGO PROJECT

root directory : folder containg manage.py 
inner project folder: same folder under root directory

__init__.py:::used to make the folder (containg it) python package

wsgi.py::: WSGI(Web Server Gateway Interface):: provides(works as) interface between web application and web server (only for synchronous)

asgi.py:::ASGI(Asynchronous Server Gateway Interface)::successor of wsgi (provide for both synchronous and asynchronous)

seetings.py::: contains all information or data about project setting

urls.py:::contains information of url attached with application

manage.py:::command-line utility of django

templates::: contains all html files(template files) *we create this

### STRUCTURE OF DJANGO APPLICATION
migration.py::: contains all the files generated after running makemigration command

admin.py::: used to register sql table to perform CRUD form Admin Application

config.py::: used to configure applications

models.py::: used to create the model class

tests.py::: used to create test cases

views.py:::used to create view(all business logic)
###### EXTRA NOTES
f string in python is like using $ in c#
