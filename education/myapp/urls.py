from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'newss'
urlpatterns = [
	url(r'^edu/', views.index, name = 'api_search'),
	url(r'^input/', views.input, name = 'inputdata'),
	url(r'^input1/', views.input1),
	url(r'^input2/', views.input2)
]
