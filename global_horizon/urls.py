"""
URL configuration for global_horizon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.contrib import admin
from django.urls import path, include
from dotenv import load_dotenv

from newspapers_tracker.views import SingUpView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("newspapers_tracker.urls", namespace="newspapers_tracker")),
    path("registration/", include("django.contrib.auth.urls")),
    path("register/", SingUpView.as_view(), name="register")
]

load_dotenv()

if os.environ.get("DJANGO_SETTINGS_MODULE", None) == "global_horizon.settings.dev":
    from debug_toolbar.toolbar import debug_toolbar_urls
    urlpatterns += debug_toolbar_urls()
