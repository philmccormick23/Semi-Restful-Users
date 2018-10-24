from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime 
from django.contrib import messages
from django.utils.crypto import get_random_string
import random
from .models import *
# the index function is called when root is visited

def index(request):
    dictionary = {
        'users' : User.objects.all()
    }
    
    return render(request,'index.html', dictionary)
    
def user(request, id):
    context = {
        'user' : User.objects.get(id=id)
    }

    return render(request,'user.html', context)

def process(request, methods=['POST']):
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], tags=request.POST['tags'])
    return redirect('/')

def new(request):
    dictionary = {
        'users' : User.objects.all()
    }
    return render(request,'new.html', dictionary)

def edit(request, id):
    context = {
        'user' : User.objects.get(id=id)
    }
    return render(request,'edit.html', context)

def update(request, id):
    b=User.objects.get(id=id)
    b.first_name=request.POST['first_name']
    b.last_name=request.POST['last_name']
    b.email=request.POST['email']
    b.save()
    print(b.tags.all())
    return redirect('/')

def tag(request, id):
    user1=User.objects.get(id=id)
    user2=User.objects.get(id=13)  ##Dummy user (can be startup, job, or deal)
    userTags=user1.tags.all()
    #print(userTags)
    user2Tags=user2.tags.all()
    #print(user2Tags)

    startupTags=User.objects.get(id=13).tags.all()[0]
    scores = User.objects.get(id=id).scores.all()
    ownTags = []
    for s in scores:
        ownTags+= [s.tag]
    #print(ownTags)
    print(type(startupTags))

    print(startupTags)
    for tag in startupTags.tag:
        print(type(tag))
        print(tag)
        if tag in ownTags:
            b=scores.get(tag=tag)
            b.score += 1
            b.save()
        else:
            Scores.objects.create(tag=tag, user=user1) #######adds startup tags to user
    userScores=User.objects.get(id=id).scores.all()
    #for score in userScores:
       # print(score.score)

    return redirect('/')

def delete(request, id):
    b=User.objects.get(id=id)
    b.delete()
    return redirect('/')



