from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from main_site.models import Book, Author, Book_Author

def index(request):
    context = {}
    return render(request, 'main_site/search_form.html', context)

def search(request):
    try:
        keyword=request.POST['research']

    except (KeyError):
        context = { 'keyword': ""}
    else:
        books = []
        authors = []
        books_and_authors = [] 

        #The keyword is an author
        books_found_when_keyword_is_an_author = Book.objects.filter(authors__name=keyword)
        if books_found_when_keyword_is_an_author:
            for b1 in books_found_when_keyword_is_an_author:
                books.append(b1.title)

        #The keyword is a book
        books_found_when_keyword_is_a_book = Book.objects.filter(title=keyword)
        if books_found_when_keyword_is_a_book:
            for b2 in books_found_when_keyword_is_a_book:
                books.append(b2.title)

        #The keyword is a genre
        books_found_when_keyword_is_a_genre = Book.objects.filter(genres__name=keyword)
        if books_found_when_keyword_is_a_genre:
            for b3 in books_found_when_keyword_is_a_genre:
                books.append(b3.title)

        #Getting the authors of the books
        if books:
            for b in books:
                authors = []
                authors_of_book_queryset = Author.objects.filter(book__title=b)
                if authors_of_book_queryset:
                    for a1 in authors_of_book_queryset:                     
                        authors.append(a1.name)
                    books_and_authors.append((b, authors))

        nb_books = len(books)

        context = { 'nb_books': nb_books,
                    'books_and_authors': books_and_authors,
                  }

    template = loader.get_template('main_site/search_result.html')
    response = template.render(context)    
    # IMPORTANT : need to use HttpResponseRedirect instead !!!
    return HttpResponse(response)

def error(request):
    return render(request, '404.html', {})