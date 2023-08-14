from django.db import models
from django.contrib.auth.models import User



import datetime
import os

# Create your models here.
class movie(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
 
    image=models.ImageField(upload_to="media")
    movie_name=models.CharField(max_length=100)
    director=models.CharField(max_length=100)
    description=models.TextField()
    release_date=models.DateField()
    

def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)


class movies(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
           
            



