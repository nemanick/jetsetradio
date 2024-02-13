from django.contrib import admin
from users.models import CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'is_staff', 'id', 'picture']

    fieldsets = (
        (None, {'fields' : ('email', 'password')}),
        (_('Personal Info'), {'fields' : ('username', 'picture', 'bio')}),
        (
            _('Permissions'),
            {'fields' : ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields' : ('last_login',)})
    )

    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('email', 'password1', 'password2')
        }),
    )

admin.site.register(CustomUser, UserAdmin)