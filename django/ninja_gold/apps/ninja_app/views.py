from django.shortcuts import render, redirect, HttpResponse
from random import randint

def index(request):
    return render(request, 'ninja_app/index.html')

def process(request):
    if request.method == 'POST':

        request.session['farm'] = randint(10,20)
        request.session['cave'] = randint(5,10)
        request.session['house'] = randint(2,5)
        request.session['casino'] = randint(0,50) 
    
    return redirect('/')