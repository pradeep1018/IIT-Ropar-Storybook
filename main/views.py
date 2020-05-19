from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Post, Comment
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
		obj.love_num += 1
	elif(id == 2):
		obj.comment_num += 1
	elif(id == 3):
		obj.share_num += 1
	obj.save()
	return redirect('home')


def CommentView(request, pk):
	post = Post.objects.get(pk = pk)
	try:
		comments = Comment.objects.filter(post_info = post)
	except:
		comments = ''
	if(request.method == 'POST'):
		comment = request.POST.get('comment')
		post = Post.objects.get(pk = pk)
		c = Comment.objects.create(comment = comment, post_info = post)
		return redirect('comment', pk = pk)
	return render(request, 'main/post_detailView.html', {'post' : post, 'comments' : comments})