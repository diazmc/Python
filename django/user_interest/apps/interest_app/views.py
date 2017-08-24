from django.shortcuts import render, redirect
from.models import User

def index(request):
    return render(request, 'interest_app/index.html')

def process(request):
    if request.method == "POST":
        User.objects.create(name=request.POST['name'])
        Interest.objects.create(interest=request.POST['interest']
        

    return redirect('/show')

def show(request):
    context = {
        "users": User.objects.all(),
        "view": view
    }
    return render(request, 'interest_app/view.html', context)