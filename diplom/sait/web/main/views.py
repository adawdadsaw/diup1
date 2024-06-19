from django.shortcuts import render
from django.views.generic import DetailView


def index (request):
    return render(request, 'main/index.html')


def about (request):
    return render (request, 'main/about.html')
