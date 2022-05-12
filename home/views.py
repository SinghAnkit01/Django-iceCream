from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from  django.contrib import messages
# from django.template import RequestContext
# from django.contrib.auth import authenticate,login
# render is for rendering template
# Create your views here.
def index(request):
    context = {
        'variable':"this is sent"
    }
    # messages.success(request,'hello')
    # return HttpResponse("This is homepage ")
    return render(request,'index.html',context)
# render always took two argument one is request and other is file-type(js,css,html)
def about(request):
    # return HttpResponse("This is about page")
    return render(request,'about.html')

def services(request):
    # return HttpResponse("This is service page")
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
    #     # creating object of Contact table and setting all the field their as name=name, email=email etc
        contact.save()
        messages.success(request,'contact form submitted successfully!')
        
    return render(request,'contact.html')
    #     return render(request,'contact.html')
        
        # request.POST is a dictionary and .get is a metod
    # return HttpResponse("This is contact page")
       
# this whole concept called as url dispatching
# use of templates in project
