from django.shortcuts import render

def index(request):
  print "Hello World"
  return render(request, 'hello_app/index.html')