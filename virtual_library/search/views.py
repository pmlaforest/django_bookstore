from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context

from django.urls import reverse

def index(request):
    template = loader.get_template('search/search_form.html')
    context = {}
    return HttpResponse(template.render(context, request))

def search(request):
    try:
        pk=request.POST['research']
        print(pk)
    except (KeyError):
        
        # There is a bug in this snippet.
        template = loader.get_template('search/search_result.html')
        context = {}
        response = template.render(context)
        return HttpResponse(response)
    else:
        template = loader.get_template('search/search_result.html')
        context = { 'book_id': pk}
        response = template.render(context)
        
        # IMPORTANT : need to use HttpResponseRedirect instead !!!
        return HttpResponse(response)

def error(request):
    template = loader.get_template('404.html')
    context = {}
    return HttpResponse(template.render(context, request))
