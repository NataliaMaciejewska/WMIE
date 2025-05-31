from subjects.models import FilesProject, Projects, FieldsOfStudy, FilesFieldsOfStudy
from django import forms


# class DownloadFileForm(forms.Form):
#     file_path = forms.CharField(max_length=255)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Download'))


# funkcja która przekazuje dane do formularza w html (Dodaj przedmiot)
# class SubjectsForm(forms.ModelForm):
#     class Meta:
#         model = Subjects
#         fields = '__all__'
#         labels = {
#             'name': 'Nazwa',
#             'semester': 'Semestr',
#             'specialization': 'Specjalizacja',
#             'description': 'Opis',
#             'FieldsOfStudy': 'Kierunek',
#         }


# funkcja która przekazuje dane do formularza w html (Dodaj projekt)
class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'
        labels = {
            'name': 'Nazwa',
        }


# funkcja która przekazuje dane do formularza w html (Dodaj plik do przedmiotu)
class FilesFosForm(forms.ModelForm):
    class Meta:
        model = FilesFieldsOfStudy
        fields = '__all__'  # <- wymagane!
        labels = {
            'name': 'Nazwa',
            'fos': 'Kierunek',
            'file': 'Dodaj plik',
        }


# funkcja która przekazuje dane do formularza w html (Dodaj plik do projektu)
class FilesProjectForm(forms.ModelForm):
    class Meta:
        model = FilesProject
        fields = '__all__'  # <- wymagane!
        labels = {
            'name': 'Nazwa',
            'project': 'Projekt',
            'file': 'Dodaj plik',
        }
