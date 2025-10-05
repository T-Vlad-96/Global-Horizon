from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from newspapers_tracker.forms import (
    TopicForm,
    RedactorForm,
    NewspaperForm,
    TopicSearchForm,
    RedactorSearchForm,
    NewspaperSearchForm,
    SingUpForm,
)
from newspapers_tracker.models import Topic, Newspaper, Redactor


class SingUpView(generic.CreateView):
    form_class = SingUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


@login_required
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


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    paginate_by = 5
    search_form = TopicSearchForm

    def get_context_data(self, *, object_list = ..., **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.search_form(self.request.GET)
        return context

    def get_queryset(self):
        self.queryset = super().get_queryset()
        search_form = self.search_form(self.request.GET)
        if search_form.is_valid():
            self.queryset = self.queryset.filter(
                name__icontains=search_form.cleaned_data["name"]
            )
        return self.queryset



class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    form_class = TopicForm
    success_url = reverse_lazy("newspapers_tracker:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    form_class = TopicForm
    success_url = reverse_lazy("newspapers_tracker:topic-list ")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    template_name = "newspapers_tracker/topic_confirm_delete.html"
    success_url = reverse_lazy("newspapers_tracker:topic-list")


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    paginate_by = 5
    search_form = RedactorSearchForm

    def get_context_data(self, *, object_list = ..., **kwargs):
        context = super().get_context_data()
        context["search_form"] = self.search_form(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        search_form = self.search_form(self.request.GET)
        if search_form.is_valid():
            queryset = queryset.filter(
                username__icontains=search_form.cleaned_data.get("username")
            )
        return queryset


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorForm
    success_url = reverse_lazy("newspapers_tracker:redactor-list")


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorForm
    success_url = reverse_lazy("newspapers_tracker:redactor-list")


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy(
        "newspapers_tracker:redactor-list"
    )
    template_name = "newspapers_tracker/redactor_confirm_delete.html"


class NewspaperList(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    paginate_by = 5
    search_form = NewspaperSearchForm

    def get_context_data(self, *, object_list = ..., **kwargs):
        context =super().get_context_data()
        context["search_form"] = self.search_form(self.request.GET)
        return context

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        search_form = self.search_form(self.request.GET)
        if search_form.is_valid():
            queryset = queryset.filter(
                title__icontains=search_form.cleaned_data.get("title")
            )
        return queryset


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy(
        "newspapers_tracker:newspaper-list"
    )


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy(
        "newspapers_tracker:newspaper-list"
    )


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    template_name = "newspapers_tracker/newspaper_delete_confirm.html"
    success_url = reverse_lazy("newspapers_tracker:newspaper-list")
