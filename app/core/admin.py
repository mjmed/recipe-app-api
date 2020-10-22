from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']

    # editing page
    fieldsets = (
        # 1era sección
        (None, {
            'fields': (
                'email',
                'password'
            )
        }),
        # 2da sección
        (_('Personal Info'), {
            'fields': (
                'name',
            )
        }),
        # 3era sección
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser'
            )
        }),
        # 4ta sección
        (_('Important dates'), {
            'fields': (
                'last_login',
            )
        }),
    )

    # adding page
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Tag)
