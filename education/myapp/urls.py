from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^input/', views.input)
]
