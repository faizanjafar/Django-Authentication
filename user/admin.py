from django.contrib import admin

# Register your models here.

from .models import UserAccount


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "username",
        "date_joined",
    )
