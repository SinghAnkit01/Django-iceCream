from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    # views.index means function index in views.py file of home app
    path("about",views.about, name='about'),
      path("services",views.services, name='services'),
       path("contact",views.contact, name='contact'),
]