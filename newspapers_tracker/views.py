from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from newspapers_tracker.forms import TopicForm, RedactorForm
from newspapers_tracker.models import Topic, Newspaper, Redactor


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
    return render(request, "newspapers_tracker/index.html", context=context)


class TopicListView(generic.ListView):
    model = Topic
    paginate_by = 5


class TopicCreateView(generic.CreateView):
    model = Topic
    form_class = TopicForm
    success_url = reverse_lazy("newspapers_tracker:topic-list")


class TopicUpdateView(generic.UpdateView):
    model = Topic
    form_class = TopicForm
    success_url = reverse_lazy("newspapers_tracker:topic-list ")


class TopicDeleteView(generic.DeleteView):
    model = Topic
    template_name = "newspapers_tracker/topic_confirm_delete.html"
    success_url = reverse_lazy("newspapers_tracker:topic-list")


class RedactorListView(generic.ListView):
    model = Redactor
    paginate_by = 5


class RedactorCreateView(generic.CreateView):
    model = Redactor
    form_class = RedactorForm
    success_url = reverse_lazy("newspapers_tracker:redactor-list")


class RedactorUpdateView(generic.UpdateView):
    model = Redactor
    form_class = RedactorForm
    success_url = reverse_lazy("newspapers_tracker:redactor-list")


class RedactorDetailView(generic.DetailView):
    model = Redactor


class RedactorDeleteView(generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy(
        "newspapers_tracker:redactor-list"
    )
    template_name = "newspapers_tracker/redactor_confirm_delete.html"
