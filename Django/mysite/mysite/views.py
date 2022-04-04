
from random import randrange
import re
from django.http import  HttpResponse
from django.shortcuts import render


# def index(request):
#     render(request,'index.html')
#     #return HttpResponse("<h1>python</h1>")
#     return HttpResponse(" <h1>Djongo Python </h1> <a href='https://www.w3schools.com/django/django_views.php'> Django View </a>")

def index(request):
    render(request,'index.html')

def about(request):
    return HttpResponse("About Django Python..")



def index1(request):
    return HttpResponse("Home")

 
def removed(request):
    return HttpResponse("remove")   

def capfirst(request):
    return HttpResponse("capitalize")

def nl(request):
    return HttpResponse("new line <a href='/'>back</a>")