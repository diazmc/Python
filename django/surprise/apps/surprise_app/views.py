from django.shortcuts import render, redirect, HttpResponse
import random
from random import shuffle

VALUES = ['blue', 'red', 'green', 'yellow', 'brown', 'black']


def index(request):
    return render(request, 'surprise_app/index.html')

def process(request):
    newList = []
    random.shuffle(VALUES)
    if request.method == "POST":
        a = request.POST['number']
        for i in range(0, int(a)):
            newList.append(VALUES[i])
            context = {
                "newList": newList
            }
        
    return render(request, 'surprise_app/results.html', context)

