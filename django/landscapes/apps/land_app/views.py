from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'land_app/index.html')

def photos(request, id):
    context = {
        "id": id
    }
    id = int(id)
    return render(request, 'land_app/results.html', context)


def photos(request,id):

    if id >= 1 and id < 11:
        landscape = 'snow.jpg'

    elif id > 10 and id < 21:
        landscape = 'desert.jpg'

    elif id > 20 and id < 31:
        landscape = 'forest.jpg'

    elif id > 30 and id < 41:
        landscape = 'vineyard.jpg'

    elif id > 40 and id < 51:
        landscape = 'tropical.jpg'

    