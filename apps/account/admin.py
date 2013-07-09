from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm,
    AdminPasswordChangeForm)
from django.utils.translation import ugettext, ugettext_lazy as _
from apps.account.models import User
from apps.account.forms import UserForm


class UserAdmin(UserAdminBase):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    add_form_template = 'admin/auth/user/add_form.html'
    change_user_password_template = None
    list_display = ('username', 'email', 'first_name', 'last_name', 'gender', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                        'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name','about_user', 'email', 'password')}
        ),
    )
    search_fields = ('username', 'first_name', 'last_name', 'email')

admin.site.register(User, UserAdmin)
