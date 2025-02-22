from Subjects.models import Subjects, FilesSubject, FilesProject, Projects
from django import forms


# class DownloadFileForm(forms.Form):
#     file_path = forms.CharField(max_length=255)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Download'))


#funkcja która przekazuje dane do formularza w html (Dodaj przedmiot)
class SubjectsForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = '__all__'
        labels = {
            'name': 'Nazwa',
            'semester': 'Semestr',
            'specialization': 'Specjalizacja',
            'description': 'Opis',
            'FieldsOfStudy': 'Kierunek',
        }


#funkcja która przekazuje dane do formularza w html (Dodaj projekt)
class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'
        labels = {
            'name': 'Nazwa',
        }

#funkcja która przekazuje dane do formularza w html (Dodaj plik do przedmiotu)
class FilesSubjectForm(forms.ModelForm):
    class Meta:
        model = FilesSubject
        exclude = ['counter']
        labels = {
            'name': 'Nazwa',
            'subject': 'Przedmiot',
            'file': 'Dodaj plik',
        }


#funkcja która przekazuje dane do formularza w html (Dodaj plik do projektu)
class FilesProjectForm(forms.ModelForm):
    class Meta:
        model = FilesProject
        exclude = ['counter']
        labels = {
            'name': 'Nazwa',
            'project': 'Projekt',
            'file': 'Dodaj plik',
        }
