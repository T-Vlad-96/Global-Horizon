from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Redactor, Topic, Newspaper


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    pass


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    pass
