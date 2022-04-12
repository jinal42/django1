from django.http import HttpResponse
from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def v2(req):
      return HttpResponse("this is view 2  ...")

def v3(request):
      return HttpResponse("this is view 3 ..")

      