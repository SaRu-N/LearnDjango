### Create virtual Environment
conda create --name anyname
### to activate
conda activate anyname //djnago3
### to deactivate
conda deactivate
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

### Define url name for view
form course import views
-->innerProject-->urls.py-->URL_PATTERNS: add path('route/',views_path)
path(route,views,kwargs=None,name=None)

### STRUCTURE OF DJANGO PROJECT
root directory : folder containg manage.py 
inner project folder: same folder under root directory

__init__.py:::used to make the folder (containg it) python package

wsgi.py::: WSGI(Web Server Gateway Interface):: provides(works as) interface between web application and web server (only for synchronous)

asgi.py:::ASGI(Asynchronous Server Gateway Interface)::successor of wsgi (provide for both synchronous and asynchronous)

seetings.py::: contains all information or data about project setting

urls.py:::contains information of url attached with application

manage.py:::command-line utility of django

### STRUCTURE OF DJANGO APPLICATION
migration.py::: contains all the files generated after running makemigration command

admin.py::: used to register sql table to perform CRUD form Admin Application

config.py::: used to configure applications

models.py::: used to create the model class
 
tests.py::: used to create test cases

views.py:::used to create view(all business logic)
##### STEPS
>create project
>create app
>add/install app in project
>create a view
>add url path of view

######EXTRA NOTES
f string in python is like using $ in c#
