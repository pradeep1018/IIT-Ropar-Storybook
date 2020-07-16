from django.db import models
import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.TextField(default='-')
    date = models.DateTimeField(null = True,auto_now = True)
    image_format = models.BooleanField(null = True)
    thought = models.TextField(default='-')
    picurl = models.TextField(default='-')
    picname = models.TextField(default='-')
    videourl = models.TextField(default = '-')
    videoname = models.TextField(default = '-')
    share_num = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)
    love_num = models.IntegerField(default=0)

    def __str__(self):
        return self.title + ' | ' + str(self.pk)

class Comment(models.Model):
    date = datetime.date.today()
    date = date = models.DateField(default = date.today)
    comment = models.TextField(default = '-')
    post_info = models.ForeignKey(Post, default='-', on_delete = models.SET_DEFAULT, verbose_name = 'POST')


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





    