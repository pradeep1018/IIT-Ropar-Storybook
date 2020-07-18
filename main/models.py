from django.db import models
import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    User = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='uploader')
    title = models.TextField(default='-')
    date = models.DateTimeField(null = True,auto_now = True)
    image_format = models.BooleanField(null = True)
    thought = models.TextField(default='-')
    picurl = models.TextField(default='-')
    picname = models.TextField(default='-')
    videourl = models.TextField(default = '-')
    videoname = models.TextField(default = '-')
    comment_num = models.IntegerField(default=0)
    love_num = models.IntegerField(default=0)

    def __str__(self):
        return self.title + ' | ' + str(self.pk)


class Generaldetails(models.Model):
    User = models.OneToOneField(User,on_delete=models.SET_NULL, null=True, blank=True)
    profilepicurl = models.TextField(default='-')
    profilepicname = models.TextField(default='-')        

class Like(models.Model):
    User = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='likeusr')
    post = models.ForeignKey(Post,on_delete=models.SET_NULL,null=True,related_name='likedpost')
    date = date = models.DateTimeField(null = True,auto_now = True)

class Comment(models.Model):
    User = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='cmntusr')
    usr_det = models.ForeignKey(Generaldetails,on_delete=models.SET_NULL,null=True,related_name='det')
    post = models.ForeignKey(Post,on_delete=models.SET_NULL,null=True,related_name='cmntpost')
    date = models.DateTimeField(null = True,auto_now = True)
    comment = models.TextField(default = '-')


class Wallmessage(models.Model):
    writer = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='writer')
    reciever = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='reciever')
    body = models.TextField()
    time = models.DateTimeField(null = True,auto_now = True)

    def __str__(self):
        return self.body

class Studentdetails(models.Model):
    User = models.OneToOneField(User,on_delete=models.SET_NULL, null=True, blank=True)
    Address=models.TextField(blank = True)
    Branch = models.CharField(max_length=50,null=True)
    Summary = models.TextField(blank = True)
    Mobile = models.CharField(max_length=16,null=True,blank = True)
    Website = models.CharField(max_length=100,null=True,blank = True)







    