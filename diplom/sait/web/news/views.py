from django.shortcuts import render
from .models import Artiles
from django.views.generic import DetailView


def news_home(request):
    news = Artiles.objects.order_by('date')
    return render (request, 'news/news_home.html', {'news': news})

class NewDetailView(DetailView):
    model = Artiles
    template_name = 'news/details_views.html'
    context_object_name = 'artiles'