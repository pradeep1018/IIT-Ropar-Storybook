from django.urls import path
from . import views
from django.shortcuts import render, redirect


urlpatterns = [

	path('',views.HomeView,name = 'home'),
	path('',views.PostView,name = 'post')


]

