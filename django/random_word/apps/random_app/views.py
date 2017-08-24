from django.shortcuts import render, redirect
import random

a = ['blue', 'red', 'green', 'yellow', 'brown', 'black']
def index(request):
    return render(request, 'random_app/index.html')

def create(request):
   
    if 'counter' in request.session:
        request.session['counter'] += 1
        request.session['random'] = random.choice(a)

    else:
        request.session['counter'] = 1

    return redirect('/')