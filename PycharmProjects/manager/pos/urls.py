
from django.contrib import admin
from django.urls import path
from pos import views

urlpatterns = [

    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('team/', views.team, name='team'),
    path('info/', views.info, name='info'),
    path('other services/', views.other, name='other'),
    path('Next Team/', views.next, name='Next'),
    path('address/', views.address, name='address'),
    path('client/', views.client, name='client'),
    path('home/', views.home, name='home'),
]
