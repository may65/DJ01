from django.shortcuts import render

# Create your views here.
# myapp/views.py

from django.http import HttpResponse

def empty_view(request):
    return HttpResponse("<h1>Страница Empty</h1><p>Содержимое для страницы Empty.</p>")

def data_view(request):
    return HttpResponse("<h1>Страница Data</h1><p>Содержимое для страницы data.</p>")


def test_view(request):
    return HttpResponse("<h1>Страница Test</h1><p>Содержимое для страницы test.</p>")