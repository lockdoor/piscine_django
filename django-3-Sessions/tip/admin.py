from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('reputation',)}),
    )
    list_display = UserAdmin.list_display + ('reputation',)

admin.site.register(CustomUser, CustomUserAdmin)
