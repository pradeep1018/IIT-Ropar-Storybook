from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Post, Comment
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def HomeView(request):
    post = Post.objects.all()
    Name = request.user.first_name
    return render(request,'main/home.html', {'posts' : post,'name':Name})

def LoginView(request):
    # post = Post.objects.all()
    if(request.method=='POST'):
        username = request.POST['username']
        password = request.POST['pass']
        print(username,password)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect(HomeView)


    return render(request,'main/login-page.html')

def WallView(request):

    return render(request,'main/wall.html')


def BatchView(request):

    return render(request,'main/batch.html')        

def SignupView(request):
    # post = Post.objects.all()
    message = None
    if(request.method=='POST'):
        username = request.POST['username']
        password = request.POST['pass']
        password2 = request.POST['pass2']

        if password2==password:
            try:
                user = User.objects.create(
                username=username
                )
                user.set_password(password)
                user.first_name = request.POST['name']
                user.save()
                login(request,user)
                return redirect(HomeView)
            except:
                message = "This username has already been taken. Please choose another username."
                return render(request,'main/signup-page.html',{'message':message})
        else:
            message = "The passwords do not match, please re-enter it correctly"
                    

    return render(request,'main/signup-page.html',{'message':message})  

def Logout(request):
    logout(request)
    return redirect(LoginView)        

def GalleryView(request):
    post = Post.objects.all()
    return render(request,'main/gallery.html',{"posts":post})

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