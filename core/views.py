from django.shortcuts import render
from django.urls import get_resolver

from subjects.models import Application


def index(request):
    app_name = Application.objects.first().name

    app_description = Application.objects.first().description

    background_img = Application.objects.first().background_path

    return render(request, 'index.html',
                  {'background_image': background_img, 'app_name': app_name, 'app_description': app_description})


def homepage(request):
    urlpatterns = get_resolver().url_patterns
    return render(request, 'homepage.html', {'urlpatterns': urlpatterns})
