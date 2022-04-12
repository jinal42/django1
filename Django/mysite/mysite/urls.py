"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  .import views  #from mysite import views                                    
# from demoapp import views            # import demoapp views here        

from view_1 import views as ve1    # views alias name : 've1'
from view_2 import views as v2     # views alias name : 'v2'
from view_3 import views      

 #import view function 
from view_1.views import  v1
from view_2.views import  v2,v3
from view_3.views import  v4



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.index,name='index'),
    # path('ana',views.ana,name="analyze"),
    # path('ana',views.ana,name='capfirst'),
    # path('ana',views.ana,name="removenl"),



    #  path('nl',views.nl,name="newline")

    # path('',views.index1,name='index1'),
    # path('about/',views.about,name='about'),
    # path('removed',views.removed,name='removed'),
    # path('capitalize',views.capfirst,name='capfirst'),
    # path('nl',views.nl,name="newline")


    # path('lrnDj/',views.learn_djnago),    #demoapp app. view function "learn_djnago" , "learn_python"
    # path('lrnPy/',views.learn_python)  ,  # one view function --> give mutliple route name
    # path('lrnDy/',views.learn_python) ,  

    # path('vurl1',ve1.v1),    # "vurl1":route name , "ve1": view alias , "v1": view function (in view_1 app.)
    # path('vurl2',v2.v2),     
    # path('vurl3',v2.v3),     
    # path('vurl4',views.v4),  


    path('vurl1',v1),   # "vurl1":route name , "v1": view function (in view_1 app.)
    path('vurl2',v2),   # "vurl2":route name , "v2": view function (in view_2 app.)
    path('vurl3',v3),   # "vurl3":route name , "v3": view function (in view_2 app.)
    path('vurl4',v4),
]
