from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request, 'login2_app/index.html')

def process(request):
    if request.method == "POST":
        res = User.objects.register(request.POST)

        if res['status']:
            request.session['user'] = request.POST['first_name']
            return redirect('/success')

        else:
            for i in range(0, len(res['data'])): 
                messages.error(request, res['data'][i])

    return redirect('/')

def login(request):
    if request.method == "POST":
        res = User.objects.login(request.POST)

        if res['status']:
            request.session['user'] = res['data'][0].first_name
            return redirect('/success')
        else:
            messages.error(request, res['data'][0])
            return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def success(request):
    return render(request, 'login2_app/success.html')