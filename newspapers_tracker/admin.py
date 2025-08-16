from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Redactor, Topic, Newspaper


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    list_filter = ("is_staff",)
    search_fields = ("username", "first_name", "last_name")
    fieldsets = UserAdmin.fieldsets + (
        ("Experience", {"fields": ("years_of_experience",)}),
    )
    add_fieldsets = (
        None,
        {
            "fields": (
                "username",
                "password1",
                "password2",
                "first_name",
                "last_name",
                "years_of_experience"
            ),
        },
    ),


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    pass
