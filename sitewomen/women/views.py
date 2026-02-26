from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return HttpResponse("Page women app")

def categories(request, cat_id):
    return HttpResponse(f"<h1>Page categories</h1><p>id: {cat_id}</p>")

def categories_slug(request, cat_slug):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Page categories</h1><p>slug: {cat_slug}</p>")

def archive(request, year):
    if year > 2026:
        raise Http404("Year is too new")
    return HttpResponse(f"<h1>Page archive</h1><p>year: {year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Page not found</h1><p>exception: {exception}</p>")