from Departments.models import Departments

def get_department(department_slug):
    """ Pobiera konfigurację wydziału na podstawie slug-a """
    try:
        return Departments.objects.get(slug=department_slug)
    except Departments.DoesNotExist:
        return None
