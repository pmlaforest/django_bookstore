from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from main_site.models import Book, Author, Book_Author, Genre

def index(request):
    context = {}
    return render(request, 'main_site/search_form.html', context)

def search(request, keyword:str=None):

    if keyword == None:
        try:
            keyword=request.POST['research']
            return HttpResponseRedirect(str(keyword)+"/")
            search(keyword)
        except (KeyError):
            context = { 'error_message': "Error in the search" }
            return render(request, 'main_site/search_result.html', context)     
    else:
        keyword = keyword.replace("%20", " ")
        books_and_authors = []
        books = []
        authors = []
        
        #The keyword is a name of an author
        books_by_author = Book.objects.filter(authors__name__icontains=keyword)
        if books_by_author:
            for b1 in books_by_author:
                books.append((b1.id, b1.title))

        #The keyword is a title of a book
        books_by_title = Book.objects.filter(title__icontains=keyword)
        if books_by_title:
            for b2 in books_by_title:
                books.append((b2.id, b2.title))

        #The keyword is a genre
        books_by_genre = Book.objects.filter(genres__name__icontains=keyword)
        if books_by_genre:
            for b3 in books_by_genre:
                books.append((b3.id, b3.title))

        #Getting the authors of the books
        if books:
            for b in books:
                authors = []
                authors_of_book_queryset = Author.objects.filter(book__title=b[1])
                if authors_of_book_queryset:
                    for a1 in authors_of_book_queryset:                     
                        authors.append(a1.name)
                    books_and_authors.append((b[0], b[1], authors))

        context = { 
            'books_and_authors': books_and_authors,
            'keyword': keyword
            }

        template = loader.get_template('main_site/search_result.html')
        response = template.render(context)    
        # IMPORTANT : need to use HttpResponseRedirect instead !!!
        return HttpResponse(response)

def get_info(request, book_id):
    
    authors_of_book = []
    genres_of_book = []

    book_to_display = Book.objects.get(id=book_id)

    authors_of_book_queryset = Author.objects.filter(book__title=book_to_display.title)
    authors_of_book = list(authors_of_book_queryset)

    genre_of_book_queryset = Genre.objects.filter(book__title=book_to_display.title)
    genres_of_book = list(genre_of_book_queryset)

    context = {
        'book_to_display': book_to_display,
        'authors_of_book': authors_of_book,
        'genres_of_book': genres_of_book,
    }
    return render(request, 'main_site/book_info.html', context)

def error(request):
    return render(request, '404.html', {})
