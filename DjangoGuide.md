#### Create virtual Environment
conda create --name anyname
#### To activate virtual Environment
conda activate anyname //djnago3
#### To deactivate Virtual Environment
conda deactivate

# STEPS To work in django project 

>- create project
>
>- create app
>
>- add/install app in project
>
>- create template folder in root directory
>
>- add templates directory in settings.py
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

-->seetings.py::: create variable TEMPLTES_DIR= [BASE_DIR / 'templates']

find list TEMPLATES[

'DIRS':[TEMPLATES_DIR]

]

can directly write "[BASE_DIR / 'templates']" in 'DIRS'

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
>- 

###### EXTRA NOTES
f string in python is like using $ in c#
