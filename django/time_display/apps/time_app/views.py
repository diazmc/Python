from django.shortcuts import render
from datetime import datetime


def index(request):
    context = {
        "date": datetime.now().date(),
        "time": datetime.now().time() 
    }
    return render(request, 'time_app/index.html', context)
