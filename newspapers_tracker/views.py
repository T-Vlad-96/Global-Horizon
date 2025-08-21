from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from newspapers_tracker.models import Topic, Newspaper


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    num_topics = Topic.objects.count()
    num_newspapers = Newspaper.objects.count()
    num_redactors = get_user_model().objects.count()
    context = {
        "num_topics": num_topics,
        "num_newspapers": num_newspapers,
        "num_redactors": num_redactors,
    }
    return render(
        request,
        "newspapers_tracker/index.html",
        context=context
    )
