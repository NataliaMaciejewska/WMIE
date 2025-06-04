from django.contrib import admin
from django.urls import path

from subjects.views import (diagram_view,
                            create_file_project, create_project, files_by_fos,
                            view_file_project, files_by_project, admin_panel,
                            get_project_dashboard, get_fos_dashboard, main_dashboard, create_file_fos, create_quiz,
                            add_question, quizzes_by_fos, quiz_detail, view_file_fos)
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
    path('view-file-project/<str:file_name>/<str:project_name>', view_file_project,
         name='download_file_project'),
    path('view-file-fos/<str:file_name>/<str:fos_name>', view_file_fos,
         name='download_file_fos'),
    path('diagrams/', diagram_view, name='diagrams'),
    path('files-fos/<str:fos>', files_by_fos, name='files_by_fos'),
    path('files-project/<int:id>', files_by_project, name='files_by_project'),
    path('dashboard/', main_dashboard, name='main_dashboard'),
    path('projects/<int:id>', get_project_dashboard, name='get_project_dashboard'),
    path('field-of-study/<int:id>', get_fos_dashboard, name='get_fos_dashboard'),
    path('admin/', admin_panel, name='admin_panel'),
    path('logout/', custom_logout, name='logout'),

    path('create-quiz/', create_quiz, name='create_quiz'),
    path('quiz/<int:quiz_id>/add-question/', add_question, name='add_question'),
    path('field-of-study/<int:fos_id>/quizzes/', quizzes_by_fos, name='quizzes_by_fos'),
    path('quiz/<int:quiz_id>/', quiz_detail, name='quiz_detail'),


]
