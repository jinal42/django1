from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def learn_djnago(req):
      #a=10+10
      # return HttpResponse(a)
      return HttpResponse("learning Django...")
      # return HttpResponse("<h2>learning Django...</h2>")
      
def learn_python(req):
      return HttpResponse("learning Python...")
     
      