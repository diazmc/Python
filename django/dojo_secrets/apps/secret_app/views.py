from django.shortcuts import render

def index(request):
    return render(request, 'secret_app/index.html')