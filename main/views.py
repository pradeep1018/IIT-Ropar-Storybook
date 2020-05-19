from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Post
import datetime

# Create your views here.


def HomeView(request):
	post = Post.objects.all()
	return render(request,'main/home.html', {'posts' : post})

def PostView(request):
	if(request.method == 'POST'):
		title = request.POST.get('title')
		thought = request.POST.get('thought')
		f = FileSystemStorage()
		try:
			myimage = request.FILES['images']
			imagename = f.save(myimage.name, myimage)
			imageurl = f.url(imagename)
		except:
			picurl = '-'
			picname = '-'
		try:
			myvideo = request.FILES['video']
			videoname = f.save(myvideo.name, myvideo)
			videourl = f.url(videoname)
		except:
			videourl = '-'
			videoname = '-'
		
		q = Post(title = title, thought = thought, picurl = imageurl, picname = imagename, videoname = videoname, videourl = videourl)
		q.save()

		return redirect('home')
	return render(request, 'main/post.html')

def CommunicateView(request, pk, id):
	obj = Post.objects.get(pk = pk)
	if(id == 1):
		obj.love += 1
	elif(id == 2):
		obj.likes += 1
	elif(id == 3):
		obj.share += 1
	obj.save()
	return redirect('home')


