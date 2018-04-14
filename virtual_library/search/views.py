from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context

from django.urls import reverse

from search.models import Book, Author, Book_Author

def index(request):
    template = loader.get_template('search/search_form.html')
    context = {}
    return HttpResponse(template.render(context, request))

def search(request):
    try:
        keyword=request.POST['research']

    except (KeyError):
        context = { 'keyword': ""}
    else:
        books_and_authors = [] 
        

        #The keyword is an author
        books_found_when_keyword_is_an_author = Book.objects.filter(authors__name=keyword)

        if books_found_when_keyword_is_an_author:
            for b in books_found_when_keyword_is_an_author:
                books_and_authors.append((b.title, keyword))

        #The keyword is a book
        books_found_when_keyword_is_a_book = Book.objects.filter(title=keyword)
        
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
    template = loader.get_template('404.html')
    context = {}
    return HttpResponse(template.render(context, request))
