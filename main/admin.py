from django.contrib import admin
from models import *
from . import models
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as


admin.site.register(User)
admin.site.register(Employe)
admin.site.register(Patient)
admin.site.register(Room)
admin.site.register(Comment)
admin.site.register(Income)
admin.site.register(Revenu)
admin.site.register(Cassa)
admin.site.register(Operator)
admin.site.register(Departament)
admin.site.register(Equipment)
admin.site.register(Info_about_clinic)


@admin.register(models.User)
class EmployeeAdmin(User):
    list_display = ['id', 'username', 'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ('phone_number', 'full_name', 'address')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
