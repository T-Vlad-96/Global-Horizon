from django.urls import path

from newspapers_tracker.views import index, TopicListView

app_name = "newspapers_tracker"

urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topic-list")
]
