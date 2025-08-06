from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User  # Import your User model here

# Register your models here.


admin.site.site_header = "TodoBack Admin"
admin.site.site_title = "TodoBack Admin Portal"
admin.site.index_title = "Welcome to the TodoBack Admin Portal"
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    ordering = ['-date_joined']
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    search_fields = ('email', 'first_name', 'last_name', 'username')

    fieldsets = (
        (_('Información personal'), {
            'fields': ('email', 'password', 'first_name', 'last_name', 'username')
        }),
        (_('Permisos'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        (_('Fechas importantes'), {
            'fields': ('last_login',)
        }),
    )

    add_fieldsets = (
        (_('Crear nuevo usuario'), {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'username', 'is_staff', 'is_active'),
        }),
    )