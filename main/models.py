from django.db import models
import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your models here.

class Post(models.Model):
    title = models.TextField(default='-')
    date = datetime.date.today()
    thought = models.TextField(default='-')
    picurl = models.TextField(default='-')
    picname = models.TextField(default='-')
    videourl = models.TextField(default = '-')
    videoname = models.TextField(default = '-')
    date = models.DateField(default = date.today)
    share = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    love = models.IntegerField(default=0)

    def __str__(self):
        return self.title + ' | ' + str(self.pk)
