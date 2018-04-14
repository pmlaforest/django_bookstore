from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

<<<<<<< HEAD
from search.models import Book, Author, Book_Author
=======
from .models import Livre
>>>>>>> 61dbf927ac49042a8d994b18309a6451cf43ea39

def index(request):
    context = {}
    return render(request, 'search/search_form.html', context)

def search(request):
    try:
<<<<<<< HEAD
        keyword=request.POST['research']

=======
        keywords=request.POST['research']
        query_results = Livre.objects.filter(livre_nom__icontains=keywords)
>>>>>>> 61dbf927ac49042a8d994b18309a6451cf43ea39
    except (KeyError):
        context = { 'keyword': ""}
    else:
<<<<<<< HEAD
        books_and_authors = [] 
        

        #The keyword is an author
        books_found_when_keyword_is_an_author = Book.objects.filter(authors__name=keyword)

        if books_found_when_keyword_is_an_author:
            for b in books_found_when_keyword_is_an_author:
                books_and_authors.append((b.title, keyword))

        #The keyword is a book
        books_found_when_keyword_is_a_book = Book.objects.filter(title=keyword)
=======
        template = loader.get_template('search/search_result.html')
        context = { 
            'query_results': query_results,
            'keywords': keywords
            }
        response = template.render(context)
>>>>>>> 61dbf927ac49042a8d994b18309a6451cf43ea39
        
        if books_found_when_keyword_is_a_book:
            for b2 in books_found_when_keyword_is_a_book:
                author_of_book = Author.objects.filter(book__title=b2)
                for author in author_of_book:         
                    books_and_authors.append((b2, author.name))

        nb_books = len(books_and_authors)

        context = { 'nb_books': nb_books,
                    'books_and_authors': books_and_authors,
                  }

    template = loader.get_template('search/search_result.html')
    response = template.render(context)    
    # IMPORTANT : need to use HttpResponseRedirect instead !!!
    return HttpResponse(response)

def error(request):
    return render(request, '404.html', {})
