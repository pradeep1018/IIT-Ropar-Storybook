from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.


def HomeView(request):

	return render(request,'main/home.html')