from django.urls import path

from newspapers_tracker.views import index

app_name = "newspapers_tracker"

urlpatterns = [
    path("", index, name="index")
]
