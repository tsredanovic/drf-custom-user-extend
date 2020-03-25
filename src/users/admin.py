from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ('email', 'name', 'is_staff', 'is_active', )
    list_filter = ('is_staff', 'is_active', )
    search_fields = ('email', 'name', )
    ordering = ('email', )

    add_form = CustomUserCreationForm
    add_fieldsets = (
        ('General', {
            'fields': ('email', 'name', )
        }),
        ('Password', {
            'fields': ('password1', 'password2', )
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', )
        }),
    )

    form = CustomUserChangeForm
    fieldsets = (
        ('General', {
            'fields': ('email', 'name', )
        }),
        ('Password', {
            'fields': ('password', )
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', )
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
