from django.utils.deprecation import MiddlewareMixin
from Departments.utils import get_department

class DepartmentMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """ Dodaje konfigurację wydziału do requesta na podstawie domeny """
        subdomain = request.get_host().split(".")[0]  # dept1.example.com → dept1
        request.department_slug = subdomain
        request.department = get_department(subdomain)
