from email import message

import django
from django.contrib.auth.decorators import login_required
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from.forms import Postroomform, Galleryform
from django.db.models import Q
from .models import Gallery, Message, Postroom, Type_of_c, Message
from django.contrib.auth.forms import UserCreationForm



#postrooms = [
#    {'id': 1, 'name':'design 1'},
#    {'id': 2, 'name':'design 2'},
#    {'id': 3, 'name':'design 3'},
#]

def loginpage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'No user with this username & password!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else :
            messages.error(request, 'Username or password does not exist!')
            

    context={'page': page}
    return render (request , 'base/login_register.html', context)

def logoutuser(request):
    logout(request)
    return redirect('home')

def registerpage(request):
    form = UserCreationForm()
    context = {'form':form}
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.usernamw = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else :
            messages.error(request, 'An error ocured during registration')

            
    return render(request, 'base/login_register.html', context)

def home (request):
    q= request.GET.get('q') if request.GET.get('q') != None else ''
    postrooms = Postroom.objects.filter(
        Q(type_of_c__name__icontains = q)|
        Q(name__icontains=q)|
        Q(description__icontains=q) )
    post_count = postrooms.count()
    type_of_cs = Type_of_c.objects.all()
    postroom_messages = Message.objects.filter(Q(postroom__type_of_c__name__icontains=q))
    context = {'postrooms':postrooms, 'type_of_cs':type_of_cs, 'post_count': post_count, 'postroom_messages':postroom_messages} 
    return render (request, 'base/home.html', context)
    

def postroom (request, pk):
    postroom = Postroom.objects.get(id = pk)
    postroom_messages = postroom.message_set.all()
    participants = postroom.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            postroom=postroom,
            body=request.POST.get('body')
        )
        postroom.participants.add(request.user)
        return redirect('postroom', pk=postroom.id)
    context = {'postroom': postroom, 'postroom_messages':postroom_messages, 'participants':participants}
    return render(request, 'base/postroom.html',context)

def userprofile(request, pk ):

    user = User.objects.get(id=pk)
    postrooms = user.postroom_set.all()
    postroon_messages = user.message_set.all()
    type_of_cs = Type_of_c.objects.all()
    context = {'user':user, 'postrooms':postrooms, 'postroom_messages':postroon_messages, 'type_of_cs':type_of_cs}
    return render(request , 'base/profile.html',context)

@login_required(login_url='/login')
def createPostroom(request):
    form = Postroomform()   
    if request.method == 'POST':
        form = Postroomform(data = request.POST, files=request.FILES)
        if form.is_valid():
            postroom = form.save(commit = False)
            postroom.host = request.user
            postroom.save()
            return redirect('home')


    context={'form':form}
    return render(request , 'base/postroom_form.html', context)
@login_required(login_url='/login')
def updatepost(request, pk):
    postroom = Postroom.objects.get(id=pk) 
    form = Postroomform(instance=postroom)

    if request.user != postroom.host :
        return HttpResponse('This is not your post!')  

    if request.method == 'POST':
        form = Postroomform(request.POST, instance=postroom)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/postroom_form.html', context)
@login_required(login_url='/login')
def deletepost(request, pk):
    postroom = Postroom.objects.get(id=pk)

    if request.user != postroom.host :
        return HttpResponse('This is not your post!')

    if request.method == 'POST':
        postroom.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':postroom})




def intropage(request):
    return render(request, 'base/images/intro.html')

def contactpage(request):
    return render(request, 'base/contact.html')

@login_required(login_url='/login')
def deletemessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user !=message.user :
        return HttpResponse('This is not your post!')

    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':postroom})

def gallery(request):
    gallerys = Gallery.objects.all()
    context = {'gallerys':gallerys}
    return render(request, 'base/gallery.html',context)

def creategallery(request):
    form = Galleryform()   
    if request.method == 'POST':
        form = Galleryform(data = request.POST, files=request.FILES)
        if form.is_valid():
            gallery= form.save(commit = False)
            
            gallery.save()
            return redirect('tg-gallery')