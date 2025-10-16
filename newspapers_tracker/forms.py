from crispy_bootstrap5.bootstrap5 import FloatingField
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Field,
    Submit,
    Button,
    Div,
    HTML,
    Row,
    Column
)
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Topic, Redactor, Newspaper


class SingUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "password1", "password2", "first_name", "last_name", "years_of_experience"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.form_class = "bg-light rounded-3 py-3 w-100"
        self.helper.field_class = "bg-white text-dark fw-bold px-3 mx-auto w-90 rounded-3"
        self.helper.form_show_labels = False
        for field in self.fields.values():
            field.help_text = None

        self.helper.layout = Layout(
            *(
                Row(
                    Column(
                        HTML(
                            f"<label class='w-30'>{self.fields.get(field).label}:</label>"
                        ),
                        Field(
                            field,
                            css_class="w-100",
                        ),
                        css_class="d-flex justify-content-start col-md-10 mx-auto"
                    )
                ) for field in self.fields
            ),
            Row(
                Column(
                    Submit(
                        name="submit",
                        value="Register",
                        css_class="btn btn-sm bg-success"
                    ),
                    Button(
                        name="cancel",
                        value="Cancel",
                        on_click="javascript:history.back()",
                        css_class="btn btn-sm bg-secondary text-white"
                    ),
                    css_class="d-flex justify-content-center col-md-10 mx-auto gap-3"
                ),
                css_class="mt-3"
            )
        )


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "bg-primary bg-gradient rounded-pill"
        self.helper.label_class = "text-white text-center fw-bold"
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Field(
                "name",
                wrapper_class="pt-3",
                css_class="bg-white text-dark fw-bold w-50 mx-auto",
                placeholder="Enter Topic Name",
            ),
            Submit(
                "submit",
                "Add",
                css_class="bg-white text-dark"
            ),
            Button(
                "button",
                "Cancel",
                css_class="btn btn-secondary bg-gradient",
                onclick="javascript:history.back()"

            )
        )


class RedactorFormCrispyStyleMixin:

    def _setup_helper(self):
        self.helper = FormHelper()
        self.helper.form_class = "w-75 mx-auto rounded-3 bg-primary bg-gradient mt-1 p-1"
        self.helper.label_class = "form-label text-dark"
        self.helper.form_show_labels = False
        for field in self.fields.values():
            field.help_text = None

        self.helper.layout = Layout(
            *(
                Row(
                    Column(
                        FloatingField(
                            field,
                            css_class="form-control bg-white text-dark rounded-3 fw-bold fs-5 px-2 mt-3",
                        ),
                        css_class="col-md-5 mx-auto"
                    )
                ) for field in self.fields if field not in ["years_of_experience", ]
            ),
            Row(
                Column(
                    Div(
                        HTML(
                            f"<label class='form-label text-white text-start fw-bold'>"
                            f"{self.fields.get('years_of_experience').label}:"
                            f"</label>"
                        ),
                        Field(
                            "years_of_experience",
                            css_class="form-control w-30 bg-white text-dark fw-bold fs-5 px-2 mt-3"
                        ),
                        css_class="d-flex justify-content-center align-items-center gap-3"
                    ),
                )
            ),
            Row(
                Column(
                    Div(
                        Submit(
                            "submit",
                            "Save",
                            css_class="btn btn-md btn-white text-dark btn-gradient"
                        ),
                        Button(
                            "cancel",
                            "Cancel",
                            onclick="javascript:history.back()",
                            css_class="btn btn-md btn-danger btn-gradient"
                        ),
                        css_class="d-flex justify-content-center gap-5"
                    )
                ),
                css_class="mt-3"
            )
        )


class RedactorCreateForm(UserCreationForm, RedactorFormCrispyStyleMixin):
    class Meta:
        model = Redactor
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "years_of_experience",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super()._setup_helper()


class RedactorUpdateForm(forms.ModelForm, RedactorFormCrispyStyleMixin):
    class Meta:
        model = Redactor
        fields = ["username", "email", "first_name", "last_name", "years_of_experience"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super()._setup_helper()


class NewspaperForm(forms.ModelForm):
    topic = forms.ModelChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.RadioSelect(),
        required=False
    )
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = Newspaper
        fields = [
            "title",
            "topic",
            "content",
            "publishers"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "w-75 mx-auto bg-primary bg-gradient rounded-3 p-3 mt-3"
        self.helper.label_class = "fw-bold text-white"
        self.helper.field_class = "form-control w-100 bg-white text-dark"
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Row(
                Column(
                    Div(
                        HTML(
                            f"<label class='text-white fw-bold fs-3'>"
                            f"{self.fields.get('title').label}:"
                            f"</label>"
                        )
                    ),
                    css_class="col-md-2"
                ),
                Column(
                    Div(
                        Field(
                            "title",
                            css_class="p-2 fw-bold fs-5"
                        ),
                    ),
                    css_class="col-md-10"
                ),
                css_class="container-fluid align-items-center"
            ),
            Row(
                Column(
                    Div(
                        HTML(
                            f"<label class='text-white fw-bold'>Topics</label>"
                        ),
                        css_class="text-center"
                    ),
                    Div(
                        Field(
                            "topic",
                        ),
                        css_class="scroll-box bg-white",
                    )
                ),
                Column(
                    Div(
                        HTML(
                            f"<label class='text-white fw-bold'>Publishers</label>",
                        ),
                        css_class="text-center"
                    ),
                    Div(
                        Field(
                            "publishers",
                        ),
                        css_class="scroll-box bg-white"
                    )
                ),
                css_class="container-fluid"
            ),
            Row(
                Column(
                    Div(
                        HTML(
                            "<label class='text-white fw-bold m-auto fs-3'>"
                            "Newspaper Text"
                            "</label>"
                        ),
                        css_class="text-center mb-1"
                    ),
                    Div(
                        Field(
                            "content",
                            css_class="p-2"
                        )
                    ),
                    css_class="col-md-12 pt-3"
                ),
                css_class="container-fluid"
            ),
            Row(
                Column(
                    Div(
                        Submit(
                            "submit",
                            value="Save",
                            css_class="btn btn-md btn-success bg-gradient rounded-3"
                        )
                    ),
                    css_class="col-md-3"
                ),
                Column(
                    Div(
                        Button(
                            "cancel",
                            value="Cancel",
                            css_class="btn btn-md btn-secondary bg-gradient rounded-3",
                            onclick="javascript:history.back()"
                        ),
                    ),
                    css_class="col-md-3"
                ),
                css_class="container-fluid justify-content-center mx-auto"
            )
        )


class SearchFormMixin(forms.Form):
    def _helper_setup(self):
        self.helper = FormHelper()
        self.helper.form_method = "GET"
        self.helper.form_class = "w-50"
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Div(
                Div(
                    Field(
                        [i for i in self.fields.keys()][0],
                        css_class="border border-1 rounded-0 px-2"
                    ),
                ),
                Div(
                    Submit(
                        "submit",
                        value="🔍",
                        css_class="border border-1 rounded-0"
                    )
                ),
                css_class="container-fluid input-group"
            )
        )


class TopicSearchForm(SearchFormMixin):
    name = forms.CharField(
        required=False,
        label="",
        max_length=60,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name"
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super()._helper_setup()


class RedactorSearchForm(SearchFormMixin):
    username = forms.CharField(
        required=False,
        label="",
        max_length=60,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username"
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super()._helper_setup()


class NewspaperSearchForm(SearchFormMixin):
    title = forms.CharField(
        required=False,
        label="",
        max_length=60,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by title"
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super()._helper_setup()
