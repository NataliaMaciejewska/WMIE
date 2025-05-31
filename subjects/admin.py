from django.contrib import admin
from .models import Projects, FilesProject, FieldsOfStudy

# W tym pliku należy zarejestrować utworzone klasy-tabele w models.py, aby były dostępne w panelu administratora

admin.site.register(FieldsOfStudy)
admin.site.register(Projects)
admin.site.register(FilesProject)

