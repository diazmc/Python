from django.shortcuts import render
from .models import Books

def index(request):
    # Books.objects.create(title='book1', author='AB', category='comedy')
    # Books.objects.create(title='book2', author='CA', category='action')
    # Books.objects.create(title='book3', author='CD', category='adventure')
    # Books.objects.create(title='book4', author='BS', category='action')
    # Books.objects.create(title='book5', author='ES', category='adventure')

    books = Books.objects.all()

    for book in books:
        print book.title, book.author, book.published_date, book.category, book.in_print
    return render(request, 'book_app/index.html')