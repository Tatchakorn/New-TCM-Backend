from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Employee, EmployeeWorkSchedule


class CustomEmployeeAdmin(UserAdmin):
    model = Employee
    ordering = ('-username',)
    list_display = ('email', 'username', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username',)}),
        ('Permission', {'fields': ('is_staff', 'is_active')}),
    )


admin.site.register(Employee, CustomEmployeeAdmin)

admin.site.register(EmployeeWorkSchedule)
