
from random import randrange

from django.http import  HttpResponse
from django.shortcuts import render


# def index(request):
#     render(request,'index.html')
#     #return HttpResponse("<h1>python</h1>")
#     return HttpResponse(" <h1>Djongo Python </h1> <a href='https://www.w3schools.com/django/django_views.php'> Django View </a>")

def index(request):
    return render(request,'index.html')

   #di={'name':'jinal','place':'surat'}
   #return render(request,'index.html',di)

# def about(request):
#     return HttpResponse("About Django Python..")

# import demoapp views here
# def index1(request):
#     return HttpResponse("Home")

 
# def removed(request):
#     return HttpResponse("remove")   

# def capfirst(request):
#     return HttpResponse("capitalize")




# def nl(request):
#     usertxt=request.GET.get('text')
#     if usertxt:
#         print("getting value--------",usertxt)
#     else:
#         usertxt = 'default'
#         print('_______________________________',usertxt)
#     return HttpResponse("new line")
#     return HttpResponse("new line <a href='/'>back</a>")



def ana(request):
    usertxt=request.GET.get('text','default')

    rem=request.GET.get('ana','off')
    fullcaps=request.GET.get('fullcaps','off')
    rmln=request.GET.get('removeline','off')
    rmsp=request.GET.get('removespace','off')



    # print(rem)
    # print(rm)


#     analyzed=usertxt
    if rem=='on':
     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''    
     analyzed=""
     for char in usertxt:
          if char not in punctuations:
               analyzed=analyzed+char
     para={'purpose':'removing Punctuations ','analyzed_text':analyzed}
     
     #     if usertxt:
     #          print("getting value--------",usertxt)
     #     else:
     #          usertxt = 'default'
     #          print('_____________________',usertxt)
     
     #     return HttpResponse("analyze..")
     return render(request,'analyze.html',para)

    elif(fullcaps=='on'):
     analyzed=""
     for char in usertxt:
        analyzed=analyzed+char.upper()
     para={'purpose':'upper case ','analyzed_text':analyzed}
     return render(request,'analyze.html',para)

    elif(rmln=='on'):
     analyzed=""
     for char in usertxt:
        if char !="\n":
          analyzed=analyzed+char
     para={'purpose':'remove new line ','analyzed_text':analyzed}
     return render(request,'analyze.html',para)
    elif(rmsp=='on'):
        analyzed=""
        for index,char in enumerate(usertxt):
         if not(usertxt[index] == " " and usertxt[index+1]==" "):
          analyzed=analyzed+char
        para={'purpose':'remove space','analyzed_text':analyzed}
        return render(request,'analyze.html',para)

    else:
         return HttpResponse("Error...") 



