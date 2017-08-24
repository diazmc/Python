from django.shortcuts import render, redirect

def index(request):
    return render(request, 'survey_app/index.html')

def process(request):
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comments'] = request.POST['comments']
        request.session['counter'] += 1
        return redirect('/result')

    else: 
        request.session['counter'] = 1
        return redirect('/result')

def results(request):
    return render(request, 'survey_app/results.html')
