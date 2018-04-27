from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, authenticate


from main_site.models import Book, Author, Book_Author, Genre
from main_site.forms import SignUpForm
from online_shop.models import Session_Cart

def index(request):

    books_to_propose = []

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    books = Book.objects.all()
    books_to_propose = list(books)

    # Render the HTML template index.html with the data in the context variable.
    context= {'num_visits':num_visits,
              'books_to_propose': books_to_propose
             }
    return render(request, 'main_site/index.html', context)

def search(request, keyword:str=None):

    if keyword == None:
        try:
            keyword=request.POST['research']
            return redirect("main_site:search", keyword)
            #search(keyword)
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

        return render(request, 'main_site/search_result.html', context)

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

# def signin(request):
#     context = {}
#     return render(request, 'main_site/signin_form.html', context)

# def signup(request):
#     context = {}
#     return render(request, 'main_site/signup_form.html', context)

def auth(request):

    return HttpResponse("The auth/ automatic redirection is set in \
                        settings.py as LOGIN_REDIRECT_URL. This current message \
                        is coming from main_site.views.auth(), \
                        Succesfull login")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('main_site:index'))
    else:
        form = SignUpForm()
    return render(request, 'main_site/signup_form.html', {'form': form})


def error(request):
    return render(request, '404.html', {})
