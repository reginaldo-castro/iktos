from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class MyUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('perfil',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('perfil',)}),
    )

admin.site.register(User, MyUserAdmin)