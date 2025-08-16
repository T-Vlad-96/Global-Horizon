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
    list_display = UserAdmin.list_display + ("years_of_experience", )


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    pass
