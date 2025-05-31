from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NewUser


# wyswietlam jakie informacje chce miec w adminie jak wyswietlam uzytkownika
class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'is_active')
    list_filter = ('email', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personals', {'fields': ('voivodeship', 'city', 'sex', 'start_date',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff')
        }),
    )


admin.site.register(NewUser, UserAdminConfig)
