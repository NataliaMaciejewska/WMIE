"""
URL configuration for WMIE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Subjects.views import (create_subject, subjects_list, diagram_view, files_by_subject, getDashboard,
                            create_file_subject, create_file_project, create_project, download_file_subject,
                            download_file_project, files_by_project, getDashboardProject, admin_panel)
from Users.views import register_page, login_page
from WMIE.views import index

# W tym miejscu tworzone są ścieżki do odpowiedniego widoku, przekazywany jest endpoint oraz funkcja utworzona
# w pliku views.py, która na wejściu otrzymuje request i zwara odpowiednie dane do widoku

urlpatterns = [

    path('register/', register_page, name="register"),
    path('login/', login_page, name="login"),

    path('admin/', admin.site.urls),
    path('', index, name="home"),

    path('createSubject/', create_subject, name='create_subject'),
    path('createProject/', create_project, name='create_project'),
    path('createFileSubject/', create_file_subject, name='create_file'),
    path('createFileProject/', create_file_project, name='create_file'),
    path('download_file_subject/<str:file_name>/<str:subject_name>/<str:fos_name>', download_file_subject,
         name='download_file_subject'),

    path('download_file_project/<str:file_name>/<str:project_name>', download_file_project,
         name='download_file_project'),

    path('diagrams/', diagram_view, name='diagrams'),

    path('files_subject/<str:subject>/<str:fos>', files_by_subject, name='files_by_subject'),
    path('files_project/<str:subject>', files_by_project, name='files_by_project'),
    path('dashboard/', subjects_list, name='subjects_list'),
    path('subjects/<str:fos_name>', getDashboard, name='subjects'),
    path('projects/<str:project_name>', getDashboardProject, name='getDashboardProject'),

    path('admin/', admin_panel, name='admin_panel')
]
