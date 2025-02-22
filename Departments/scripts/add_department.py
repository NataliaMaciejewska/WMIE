
import os

import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WMIE.settings") # Zamień "WMIE" na swoją aplikację główną

django.setup()

from Departments.models import Departments

departments = [
    {"name": "Wydział Artystyczny", "slug": "WA", "contact_email": "Sekretariat@wa.uz.zgora.pl"},
    {"name": "Wydział Humanistyczny", "slug": "WH",  "contact_email": "sekretariat@wh.uz.zgora.pl"},
    {"name": "Wydział Lekarski i Nauk o Zdrowiu - Collegium Medicum", "slug": "CM",  "contact_email": "sekretariatinm@cm.uz.zgora.pl"},
    {"name": "Wydział Nauk Inżynieryjno-Technicznych", "slug": "WIT",  "contact_email": "sekretariat@wiea.uz.zgora.pl"},
    {"name": "Wydział Nauk Prawnych i Ekonomicznych", "slug": "WPE",  "contact_email": "sekretariat@wnpe.uz.zgora.pl"},
    {"name": "Wydział Nauk Społecznych", "slug": "WS",  "contact_email": "sekretariat@wns.uz.zgora.pl"},
    {"name": "Wydział Nauk Ścisłych i Przyrodniczych", "slug": "WSP",  "contact_email": "sekretariat@wnsp.uz.zgora.pl"},
]

for dept in departments:
    obj, created = Departments.objects.get_or_create(**dept)
    if created:
        print(f"Dodano: {obj.name}")
    else:
        print(f"{obj.name} już istnieje!")
