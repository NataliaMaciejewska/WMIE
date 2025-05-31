from django.contrib import admin
from django.urls import path

from subjects.views import (diagram_view,
                            create_file_project, create_project, files_by_fos,
                            download_file_project, files_by_project, admin_panel,
                            get_project_dashboard, get_fos_dashboard, main_dashboard, create_file_fos)
from users import views
from users.views import login_page, custom_logout
from core.views import index

# W tym miejscu tworzone są ścieżki do odpowiedniego widoku, przekazywany jest endpoint oraz funkcja utworzona
# w pliku views.py, która na wejściu otrzymuje request i zwara odpowiednie dane do widoku

SESSION_ENGINE = "django.contrib.sessions.backends.db"

urlpatterns = [

    path('login/', login_page, name="login"),
    path('admin/', admin.site.urls),
    path('', index, name="home"),
    path('create-project/', create_project, name='create_project'),
    path('create-file-project/', create_file_project, name='create_file'),
    path('create-file-fos/', create_file_fos, name='create_file'),
    path('download-file-project/<str:file_name>/<str:project_name>', download_file_project,
         name='download_file_project'),
    path('diagrams/', diagram_view, name='diagrams'),
    path('files-fos/<str:fos>', files_by_fos, name='files_by_fos'),
    path('files-project/<int:id>', files_by_project, name='files_by_project'),
    path('dashboard/', main_dashboard, name='main_dashboard'),
    path('projects/<int:id>', get_project_dashboard, name='get_project_dashboard'),
    path('field-of-study/<int:id>', get_fos_dashboard, name='get_fos_dashboard'),
    path('admin/', admin_panel, name='admin_panel'),
    path('logout/', custom_logout, name='logout'),


]
