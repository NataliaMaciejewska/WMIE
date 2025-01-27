from django.shortcuts import render
from django.urls import get_resolver


def index(request):
    return render(request, 'index.html')

def homepage(request):
    urlpatterns = get_resolver().url_patterns
    return render(request, 'homepage.html', {'urlpatterns': urlpatterns})