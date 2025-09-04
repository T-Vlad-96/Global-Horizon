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
from django.contrib.auth.forms import UserCreationForm

from .models import Topic, Redactor


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


class RedactorForm(UserCreationForm):
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
                            css_class="form-control bg-white text-dark rounded-3 fw-bold fs-5 px-2 mt-3"
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
                            css_class="btn btn-md btn-danger btn-gradient"
                        ),
                        css_class="d-flex justify-content-center gap-5"
                    )
                ),
                css_class="mt-3"
            )
        )
