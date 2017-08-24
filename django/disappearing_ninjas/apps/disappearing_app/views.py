from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'disappearing_app/index.html')

def show(request):
    return render(request, 'disappearing_app/all.html')

def display(request, color):
    ninja_color = {
        "color": color
    }
    return render(request, 'disappearing_app/ninjas.html', ninja_color)
