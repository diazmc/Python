from django.shortcuts import render

def index(request):
    return render(request, 'portfolio_app/index.html')

def testimonial(request):
    return render(request, 'portfolio_app/testimonial.html')
    