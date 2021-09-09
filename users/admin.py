from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    ordering = ('-date_joined',)
    list_display = ('email', 'username', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'role')}),
        ('Permission', {'fields': ('is_staff', 'is_active')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)