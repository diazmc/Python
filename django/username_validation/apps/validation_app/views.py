from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Username

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    return render(request, 'validation_app/index.html')

def create(request):
    if len(request.POST['username']) < 8:
        messages.add_message(request, messages.SUCCESS, "Need at least 8 characters")
        pass
    elif len(request.POST['username']) > 26:
        messages.add_message(request, messages.SUCCESS, "Too many characters!!")
        pass
    elif not EMAIL_REGEX.match(request.POST['username']):
        messages.add_message(request, messages.SUCCESS, "Username is not valid")
        pass
    else:
        Username.objects.create(name=request.POST['username'])
        messages.add_message(request, messages.SUCCESS, "The username you entered" + " " + request.POST['username'] + " " + "is valid!")
        return redirect('/show')
    
    return redirect('/')

def show(request):
    context = {
        "usernames": Username.objects.all()
    }

    return render(request, 'validation_app/success.html', context)
    