from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import *
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

@login_required
def ProfileView(request):
    user = request.user

    message = None

    # special = False

    data = Studentdetails.objects.filter(User=user)

    if not data:
        data = None
    else:
        data = data[0]    

    if request.method=='POST':
        try:
            usable = user.has_usable_password()
            curr = authenticate(username = user.username,password = request.POST['curr_password'])
            
            if not curr and usable:
                message = "The password you entered does not match your current password. Note: For new accounts it was initially set to be blank !"
                return render(request,'main/update-profile.html',{'user':user,'data':data,'message':message})


            f = FileSystemStorage()

            try:
                myimage = request.FILES['images']
                print(myimage)
                imagename = f.save(myimage.name, myimage)
                imageurl = f.url(imagename)
            except:
                imageurl = '-'
                imagename = '-'
    
            print(imageurl)
            gen = Generaldetails.objects.get(User=user)
            gen.profilepicurl = imageurl
            gen.profilepicname = imagename
            gen.save()    

            user.username = request.POST['username']

            if request.POST['new_password']==request.POST['new_password2'] and request.POST['new_password']!='':
                user.set_password(request.POST['new_password'])

            user.save()    

            if data:
                data.Address = request.POST['address']
                data.Branch  = request.POST['branch']
                data.Mobile  = request.POST['mobile']
                data.Website  = request.POST['website']
                data.Summary  = request.POST['summary']
                data.save()      


        except:
            message = "There seems to be an error in the details you have given. Please fill them carefully. If you are trying to change your username, it may be possible that it is already taken !"
            return render(request,'main/update-profile.html',{'user':user,'data':data,'message':message})
        

    return render(request,'main/update-profile.html',{'user':user,'data':data,'message':message})

@login_required
def HomeView(request):
    post = Post.objects.all()
    
    likes = []

    


    user = request.user

    for i in Post.objects.all():
        found = Like.objects.filter(post=i,User=user)
        if found:
            likes.append(True)
        else:
            likes.append(False)


    email = user.email

    data = Studentdetails.objects.filter(User = user)

    gen = Generaldetails.objects.filter(User=user)

    if not gen:
        new = Generaldetails.objects.create(User=user)
        gen = new
    else:
        gen = gen[0]    
    
    if "2018"==email[0:4] and not data:
        fresh = Studentdetails.objects.create(User = user)
        return redirect(ProfileView)
  

    return render(request,'main/home.html', {'posts' : zip(post,likes),'posts2' : zip(post,likes),'user':user,'gen':gen})

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

@login_required
def WallView(request):

    return render(request,'main/wall.html')

@login_required
def BatchView(request):

    user = request.user

    return render(request,'main/batch.html',{'user':user})        

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

def LogoutView(request):
    logout(request)
    
    return redirect(HomeView)  

@login_required
def GalleryView(request):
    post = Post.objects.all()
    likes = []

    user = request.user

    for i in Post.objects.all():
        found = Like.objects.filter(post=i,User=user)
        if found:
            likes.append(True)
        else:
            likes.append(False)

    return render(request,'main/gallery.html',{"posts":zip(post,likes),'user':user})

# @login_required
# def     

@login_required
def PostView(request):
    user = request.user
    if(request.method == 'POST'):
        title = request.POST.get('title')
        thought = request.POST.get('thought')
        f = FileSystemStorage()

        try:
            myimage = request.FILES['images']
            imagename = f.save(myimage.name, myimage)
            imageurl = f.url(imagename)
        except:
            imageurl = '-'
            imagename = '-'
        try:
            myvideo = request.FILES['video']
            videoname = f.save(myvideo.name, myvideo)
            videourl = f.url(videoname)
        except:
            videourl = '-'
            videoname = '-'
        
        q = Post(title = title, thought = thought, picurl = imageurl, picname = imagename, videoname = videoname, videourl = videourl)
        if imagename!='-':
            q.image_format = True
        else:
            q.image_format = False  

        q.User = user      
        q.save()

        return redirect('home')
    return render(request, 'main/post.html',{'user':user})

@login_required
def CommunicateView(request, pk, id):
    user = request.user
    obj = Post.objects.get(pk = pk)
    
    already = Like.objects.filter(User = user,post=obj)
    if not already:
        obj.love_num += 1
        naya = Like.objects.create(User=user,post = obj)
    else:
        already[0].delete()
        obj.love_num -=1    
    

    obj.save()
    if(id == 2):
        return redirect(GalleryView)
    else:
        return redirect(HomeView)     

@login_required
def CommentView(request, pk):
    post = Post.objects.get(pk = pk)
    gen = Generaldetails.objects.get(User=request.user)
    user = request.user
    comments = Comment.objects.filter(post = post)

    # print(comments[0])

    if(request.method == 'POST'):
        comment = request.POST['comment']
        c = Comment.objects.create(comment = comment, post = post, User=user, usr_det = gen)
        post.comment_num+=1

        post.save()
        return redirect('comment', pk = pk)
    return render(request, 'main/post_detailView.html', {'post' : post, 'comments' : comments,'user':user,'gen':gen})



