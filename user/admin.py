from django.contrib import admin
from user.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass
    # fieldsets = (
    #     (None, {"fields": ("username", "password")}),
    #     ("Información personal", {"fields": ("first_name", "last_name", "email")}),
    #     ("Permisos", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    #     ("Fechas importantes", {"fields": ("last_login", "date_joined")}),
    # )

    # list_display = ("username", "email", "first_name", "last_name", "is_staff")
    # search_fields = ("username", "email", "first_name", "last_name")
    # ordering = ("username",)
