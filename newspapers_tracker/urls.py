from django.urls import path

from newspapers_tracker.views import (
    index,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
)

app_name = "newspapers_tracker"

urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path("topics/udpate/<int:pk>/", TopicUpdateView.as_view(), name="topic-update"),

]
