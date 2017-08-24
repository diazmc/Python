from django.shortcuts import render

def index(request):
    return render(request, 'realportfolio_app/index.html')

def projects(request):
    return render(request, 'realportfolio_app/projects.html')

def aboutme(request):
    return render(request, 'realportfolio_app/aboutme.html')

def testimonials(request):
    return render(request, 'realportfolio_app/testimonials.html')
