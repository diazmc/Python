from django.shortcuts import render, redirect, HttpResponse
from .models import User, Author, Book, Review
from django.contrib import messages


def index(request):
    return render(request, 'belt_app/index.html')

def process(request):
    if request.method == "POST":
        res = User.objects.register(request.POST)

        if res['status']:
            request.session['user'] = request.POST['name']
            return redirect('/books')

        else:
            for i in range(0, len(res['data'])): 
                messages.error(request, res['data'][i])

    return redirect('/')

def login(request):
    if request.method == "POST":
        res = User.objects.login(request.POST)

        if res['status']:
            request.session['user'] = res['data'][0].name
            return redirect('/books')
        else:
            messages.error(request, res['data'][0])
            return redirect('/')
def books(request):
    if 'user' not in request.session:
        messages.error(request, "Need to register or login")
        return redirect('/')

    context = {
        "books": Book.objects.all()
    }
    return render(request, 'belt_app/bookreview.html', context)

def addbookspage(request):
    if 'user' not in request.session:
        messages.error(request, "Need to register or login!!!")
        return redirect('/')
    context = {
        "authors": Author.objects.all()
    }

    return render(request, 'belt_app/addbook.html', context)

def addbook(request):
    if request.method == "POST":

        res = Author.objects.add_author(request.POST)
        Book.objects.create(title=request.POST['title'], author=Author.objects.get(name=request.POST['author']))
       
        
    return redirect('/books')

def displayUser(request, id):
    context = {
        "id": id,
        "user": User.objects.get(id=id),
        "users": User.objects.all()
    }

    if 'user' not in request.session:
        messages.error(request, "Need to register or login!!!")
        return redirect('/')
    return render(request, 'belt_app/userinfo.html', context)

def displayBook(request, id):
    context = {
        "id": id,
        "books": Book.objects.get(id=id)
    }
    return render(request, 'belt_app/addreview.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')