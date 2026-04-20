from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template.defaultfilters import title
from django.urls import reverse
from django.template.loader import render_to_string


menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id':2, 'title': 'Скарлетт Йоханссон', 'content': 'Биография Скарлетт Йоханссон', 'is_published': False},
    {'id': 3, 'title': 'Моника Беллуччи', 'content': 'Биография Моники Беллуччи', 'is_published': True},
]

def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'women/index.html', context=data)

def about(request):
    return render(request, 'women/about.html', {'title': 'About', 'menu': menu})

def categories(request, cat_id):
    return HttpResponse(f"<h1>Page categories</h1><p>id: {cat_id}</p>")

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")

def add_page(request):
    return HttpResponse('Добавление статьи')

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse(' Авторизация ')

def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Page not found</h1><p>exception: {exception}</p>")