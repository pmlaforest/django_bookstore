from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Sale

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
    
