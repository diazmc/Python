from django.shortcuts import render, redirect, HttpResponse
from .models import Course
import datetime

def index(request):
    context = {
        "courses": Course.objects.all(),
        "action": "Remove",
        "now": datetime.datetime.now().strftime('%H:%M:%S')
    }
    return render(request, 'courses_app/index.html', context)

def create(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')

def destroy(request, id):
    context = {
        "id": id,
        "courses": Course.objects.get(id=id)
    }
    return render(request, 'courses_app/delete.html', context)

def delete(request,id):
    context = {
        "id": id,
        "del": Course.objects.get(id=id).delete()
    }
    return redirect('/')