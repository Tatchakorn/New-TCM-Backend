from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, OwnPatient, PastPatient


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    ordering = ('-start_date',)
    list_display = ('email', 'username', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'role')}),
        ('Permission', {'fields': ('is_staff', 'is_active')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(OwnPatient)
admin.site.register(PastPatient)
