from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'govindadJobsCard'
urlpatterns = [
 path('', views.newJobCardPage, name ='newJobCardPage')
]
