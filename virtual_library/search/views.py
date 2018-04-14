from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Livre

def index(request):
    context = {}
    return render(request, 'search/search_form.html', context)

def search(request):
    try:
        keywords=request.POST['research']
        query_results = Livre.objects.filter(livre_nom__icontains=keywords)
    except (KeyError):
        
        # There is a bug in this snippet.
        template = loader.get_template('search/search_result.html')
        context = {}
        response = template.render(context)
        return HttpResponse(response)
    else:
        template = loader.get_template('search/search_result.html')
        context = { 
            'query_results': query_results,
            'keywords': keywords
            }
        response = template.render(context)
        
        # IMPORTANT : need to use HttpResponseRedirect instead !!!
        return HttpResponse(response)

def error(request):
    return render(request, '404.html', {})
