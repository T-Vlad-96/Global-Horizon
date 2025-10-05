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
    RedactorDetailView,
    RedactorDeleteView,
    NewspaperList,
    NewspaperCreateView,
    NewspaperUpdateView,
    NewspaperDetailView,
    NewspaperDeleteView,
)

app_name = "newspapers_tracker"

urlpatterns = [
    # Topic routes
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path("topics/update/<int:pk>/", TopicUpdateView.as_view(), name="topic-update"),
    path("topics/delete/<int:pk>/", TopicDeleteView.as_view(), name="topic-delete"),
    # Redactor routes
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactors/create/", RedactorCreateView.as_view(), name="redactor-create"),
    path("redactors/update/<int:pk>/", RedactorUpdateView.as_view(), name="redactor-update"),
    path("redactors/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"),
    path("redactors/delete/<int:pk>/", RedactorDeleteView.as_view(), name="redactor-delete"),
    # Newspaper routes
    path("newspapers/", NewspaperList.as_view(), name="newspaper-list"),
    path("newspapers/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path("newspapers/create/", NewspaperCreateView.as_view(), name="newspaper-create"),
    path("newspapers/update/<int:pk>/", NewspaperUpdateView.as_view(), name="newspaper-update"),
    path("newspapers/delete/<int:pk>/", NewspaperDeleteView.as_view(), name="newspaper-delete"),

]
