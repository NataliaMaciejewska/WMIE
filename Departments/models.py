from django.db import models

class Departments(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, unique=True)  # Nazwa wydziału
    slug = models.SlugField(unique=True)  # dept1, dept2 - do identyfikacji
    contact_email = models.EmailField(blank=True, null=True)  # Opcjonalne dane kontaktowe

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
