from django.urls import path
from . import views
from django.shortcuts import render, redirect


urlpatterns = [

	path('',views.HomeView,name = 'home'),
	path('post/',views.PostView,name = 'post'),
	path('post/comment/<int:pk>/',views.CommentView,name = 'comment'),
	path('post/<int:pk>/<int:id>/',views.CommunicateView,name = 'communicate'),


]

