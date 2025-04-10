from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    # Optionally, you can customize the fields displayed in admin
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth',)}),
    )

admin.site.register(User, CustomUserAdmin)