from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'govindadUserAuth'
urlpatterns = [
 path('', views.loginPage, name ='loginPage'),
 path('logout', views.logoutPage, name ='logoutPage'),
]
