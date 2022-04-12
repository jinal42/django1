from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def v4(req):
      return HttpResponse("this is view 4 ...")