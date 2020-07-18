from django.db import models
import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User

#auto_now -> stores edit time, auto_now_add -> stores creation time

#model class for each post
class Post(models.Model):
    User = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='uploader')
    title = models.TextField(default='-')
    date = models.DateTimeField(null = True,auto_now_add = True)
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

# General details will store general details of everyone, for now it only has profile pic
class Generaldetails(models.Model):
    User = models.OneToOneField(User,on_delete=models.SET_NULL, null=True, blank=True)
    profilepicurl = models.TextField(default='-')
    profilepicname = models.TextField(default='-')        

#model class for each like
class Like(models.Model):
    User = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='likeusr')
    post = models.ForeignKey(Post,on_delete=models.SET_NULL,null=True,related_name='likedpost')
    date = date = models.DateTimeField(null = True,auto_now_add = True)

#model class for each comment
class Comment(models.Model):
    User = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='cmntusr')
    usr_det = models.ForeignKey(Generaldetails,on_delete=models.SET_NULL,null=True,related_name='det')
    post = models.ForeignKey(Post,on_delete=models.SET_NULL,null=True,related_name='cmntpost')
    date = models.DateTimeField(null = True,auto_now_add = True)
    comment = models.TextField(default = '-')

# model class for each wall message
class Wallmessage(models.Model):
    writer = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='writer')
    reciever = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='reciever')
    body = models.TextField()
    color = models.TextField(default="orange",null=True)
    time = models.DateTimeField(null = True,auto_now = True)

    def __str__(self):
        return self.body

# Studentdetails will store the details of the graduating batch students 
class Studentdetails(models.Model):
    User = models.OneToOneField(User,on_delete=models.SET_NULL, null=True, blank=True)
    general = models.OneToOneField(Generaldetails,on_delete=models.SET_NULL, null=True, blank=True)
    Address=models.TextField(blank = True)
    Branch = models.CharField(max_length=100,null=True)
    Summary = models.TextField(blank = True, default='-')
    Mobile = models.CharField(max_length=16,null=True,blank = True)
    Website = models.CharField(max_length=100,null=True,blank = True)







    