from django.shortcuts import render, redirect
from django.db.models import F
from .models import User, Poke
from django.contrib import messages
import bcrypt

def index(request):

    return render(request, 'login3_app/index.html')

def success(request):
    if 'id' not in request.session:
        messages.error(request, "Need to register or login")
        return redirect('/')
    
    user = User.objects.get(id=request.session['id'])

    context = {
        "user": user,
        "users": User.objects.exclude(id=request.session['id']),
        "poke": 'Poke!',
        "pokes": 'pokes'
    }
    return render(request, 'login3_app/success.html', context)

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

def poke(request, id):
    poker = User.objects.get(id=request.session['id'])
    print poker.first_name
    # User.objects.filter(id=id).update(pokes=F('pokes')+1)
    poked = User.objects.get(id=id)

    print poked.first_name
    Poke.objects.update(pokee=poked, pokes=F('pokes')+1)

    pokes = Poke.objects.all()
    return redirect('/success')

def logout(request):
    request.session.flush()
    return redirect('/')
