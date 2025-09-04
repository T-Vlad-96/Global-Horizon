from django.urls import path

from newspapers_tracker.views import (
    index,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
    RedactorListView,
    RedactorCreateView,
    RedactorUpdateView,
)

app_name = "newspapers_tracker"

urlpatterns = [
    # Topic routes
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path("topics/udpate/<int:pk>/", TopicUpdateView.as_view(), name="topic-update"),
    path("topics/delete/<int:pk>/", TopicDeleteView.as_view(), name="topic-delete"),
    # Redactor routes
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactors/create/", RedactorCreateView.as_view(), name="redactor-create"),
    path("redactors/update/<int:pk>/", RedactorUpdateView.as_view(), name="redactor-update"),

]
