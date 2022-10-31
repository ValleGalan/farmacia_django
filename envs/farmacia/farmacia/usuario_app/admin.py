from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from usuario_app.models import User
# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass

