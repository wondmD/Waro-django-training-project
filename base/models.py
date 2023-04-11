
from distutils.command.upload import upload
from django.db import models

from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Type_of_c(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
class Gallery(models.Model):
    name = models.CharField(max_length=100, null = True , blank = True)
    Gallery_image =models.ImageField(null =True, blank=True, upload_to = 'gallery_image/')
    caption = models.TextField(null = True, blank= True)

    def __str__(self):
        return self.name


class Postroom(models.Model):
    
    host = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    type_of_c = models.ForeignKey(Type_of_c, on_delete = models.SET_NULL, null = True)
    name = models.CharField(max_length=100)

    post_image = models.ImageField( null=True, blank=True, upload_to='')
    description = models.TextField(null = True, blank = True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    

    class Meta :
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name 


class Message(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    postroom = models.ForeignKey(Postroom, on_delete = models.SET_NULL, null=True)
    body  = models.TextField()
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    class Meta :
        ordering = ['updated', 'created']

    def __str__(self):
        return self.body[0:50]

