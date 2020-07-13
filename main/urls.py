from django.urls import path
from . import views
from django.shortcuts import render, redirect


urlpatterns = [

	path('',views.HomeView,name = 'home'),
	path('login/',views.LoginView,name = 'login'),
	path('logout/',views.LoginView,name = 'logout'),
	path('signup/',views.SignupView,name = 'signup'),
	path('post/',views.PostView,name = 'post'),
	path('post/comment/<int:pk>/',views.CommentView,name = 'comment'),
	path('post/<int:pk>/<int:id>/',views.CommunicateView,name = 'communicate'),
	path('gallery/',views.GalleryView,name='gallery'),

]

