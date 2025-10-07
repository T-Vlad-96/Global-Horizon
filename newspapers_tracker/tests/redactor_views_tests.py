from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from newspapers_tracker.models import Redactor

REDACTOR_LIST_VIEW_URL = reverse_lazy("newspapers_tracker:redactor-list")
REDACTOR_CREATE_VIEW_URL = reverse_lazy("newspapers_tracker:redactor-create")
REDACTOR_DETAIL_VIEW_URL = reverse_lazy(
    "newspapers_tracker:redactor-detail",
    kwargs={"pk": 1}
)
REDACTOR_UPDATE_VIEW_URL = reverse_lazy(
    "newspapers_tracker:redactor-update",
    kwargs={"pk": 1}
)
REDACTOR_DELETE_VIEW_URL = reverse_lazy(
    "newspapers_tracker:redactor-delete",
    kwargs={"pk": 1}
)
