from django.db import models

from users.models import NewUser


class FieldsOfStudy(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, blank=True, unique=True)

    class Meta:
        verbose_name = "FieldOfStudy"
        verbose_name_plural = "FieldsOfStudy"


# Utworzenie klasy generującej tabelę w bazie danych - Projekt
class Projects(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"


# Utworzenie klasy generującej tabelę w bazie danych - Pliki z projektu
class FilesProject(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, blank=True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to='uploads/', null=True, blank=True, unique=True)

    class Meta:
        verbose_name = "FileProject"
        verbose_name_plural = "FilesProjects"


# Utworzenie klasy generującej tabelę w bazie danych - Pliki z projektu
class FilesFieldsOfStudy(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, blank=True)
    fos = models.ForeignKey(FieldsOfStudy, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to='uploads/', null=True, blank=True, unique=True)

    class Meta:
        verbose_name = "FileFos"
        verbose_name_plural = "FilesFos"


class Application(models.Model):
    name = models.CharField(max_length=255, unique=True)
    background_path = models.CharField(max_length=500)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class VisitCount(models.Model):
    counter = models.IntegerField(default=0, blank=True)
    voivodeship = models.CharField(max_length=255, blank=True)
    sex = models.CharField(max_length=255, blank=True)
    fieldOfStudy = models.ForeignKey(FieldsOfStudy, on_delete=models.CASCADE, null=True)

####################################### quizy ###############

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    fos = models.ForeignKey(FieldsOfStudy, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question,related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({'✔️' if self.is_correct else '❌'})"