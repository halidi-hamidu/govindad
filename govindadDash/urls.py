from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'govindadDash'
urlpatterns = [
 path('', views.dashboardPage, name ='dashboardPage')
]
