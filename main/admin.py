from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Wallmessage)
admin.site.register(Studentdetails)
admin.site.register(Generaldetails)
admin.site.register(Like)