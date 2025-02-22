from django.db import models

class FieldsOfStudy(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "FieldOfStudy"
        verbose_name_plural = "FieldsOfStudy"


# Utworzenie klasy generującej tabelę w bazie danych - Przedmiot

class Subjects(models.Model):
    def __str__(self):
        return self.name

    class Semesters(models.IntegerChoices):
        OPTION1 = 1, 'Semestr 1'
        OPTION2 = 2, 'Semestr 2'
        OPTION3 = 3, 'Semestr 3'
        OPTION4 = 4, 'Semestr 4'
        OPTION5 = 5, 'Semestr 5'
        OPTION6 = 6, 'Semestr 6'
        OPTION7 = 7, 'Semestr 7'

    name = models.CharField(max_length=100, blank=True)
    semester = models.IntegerField(choices=Semesters.choices,
                                   default=Semesters.OPTION1, blank=False)
    specialization = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    FieldsOfStudy = models.ForeignKey(FieldsOfStudy, on_delete=models.CASCADE, null=True)


class Meta:
    verbose_name = "Subject"
    verbose_name_plural = "Subjects"


# Utworzenie klasy generującej tabelę w bazie danych - Projekt
class Projects(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"


# Utworzenie klasy generującej tabelę w bazie danych - Pliki z przedmiotów
class FilesSubject(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, blank=True)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to='uploads/', null=True, blank=True, unique=True)
    counter = models.IntegerField(default=0, blank=True)

    class Meta:
        verbose_name = "FileSubject"
        verbose_name_plural = "FilesSubject"


# Utworzenie klasy generującej tabelę w bazie danych - Pliki z projektu
class FilesProject(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, blank=True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to='uploads/', null=True, blank=True, unique=True)
    counter = models.IntegerField(default=0, blank=True)

    class Meta:
        verbose_name = "FileProject"
        verbose_name_plural = "FilesProjects"

# klasa Meta jest tworzona, by była poprawnie utworzona liczba mnoga od nazwy klasy

