from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def fees_django(request):
    return HttpResponse("This is fee structure of django tutorial")