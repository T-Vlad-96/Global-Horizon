from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Button
from .models import Topic


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
