from django.shortcuts import render, redirect 
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'login1_app/index.html')

def success(request):
    if 'id' not in request.session:
        messages.error(request, "Need to register or login")
        return redirect('/')
    
    user = User.objects.get(id=request.session['id'])

    context = {
        "user": user
    }
    return render(request, 'login1_app/success.html', context)

def process(request):
    if request.method == "POST":
        res = User.objects.register(request.POST)

        if res['status']:
            request.session['id'] = res['data'].id
            return redirect('/success')

        else:
            for error in res['data']: 
                messages.error(request, error)

    return redirect('/')

def login(request):
    if request.method == "POST":
        res = User.objects.login(request.POST)

        if res['status']:
            request.session['id'] = res['data'].id
            return redirect('/success')
        else:
            messages.error(request, "Email or password invalid")
            return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

