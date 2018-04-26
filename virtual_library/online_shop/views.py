from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import json
from django.forms.models import model_to_dict


from .models import Sale, Session_Cart

from main_site.models import Book

# Create your views here.

@login_required
def shop(request):
    sale_query = request.POST.get("research")
    if sale_query is not None:
        sale = Sale()
        sale.product = sale_query
        sale.user = request.user
        sale.save()
        return redirect(reverse('main_site:index'))
    else:
        return render(request, "online_shop/sale_form.html", {})

@login_required
def add_to_cart(request, book_id):    
    user_cart = Session_Cart.objects.get(user=request.user)
    if not user_cart:
        a = Session_Cart()
        a.user = request.user
        a.save()
        user_cart = a

    request.session["shopping_cart"] = user_cart
    request.session.modified = True

    request.session["shopping_cart"].add(book_id)
    return redirect(
        request.META.get('HTTP_REFERER','main_site:index')
    )


@login_required
def view_cart(request):
    user_cart = request.session.get("shopping_cart")
    if not user_cart:
        user_cart = Session_Cart.objects.filter(user=request.user).first()
        if not user_cart:
            a = Session_Cart()
            a.user = request.user
            a.save()
            user_cart = a
        request.session["shopping_cart"] = user_cart.id
        request.session.modified = True
    else:
        user_cart = Session_Cart.objects.get(id=request.session["shopping_cart"])

    shopping_cart = user_cart.books.all()

    shopping_cart_books = []
    for book_id in shopping_cart:
        book = Book.objects.get(id=book_id)
        shopping_cart_books.append({ "id":book.id, "title":book.title })
    context = { "books": shopping_cart_books, }


        #oi_serialized = json.dumps(oi_dict)

    return render(request, "online_shop/shopping_cart.html", context)



