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


class RedactorModelViewsPublic(TestCase):
    """
    Class to tests if the views related to
    Redactor model are available for
    unauthenticated users
    """

    @classmethod
    def setUpTestData(cls):
        cls.redactor = get_user_model().objects.create_user(
            username="test_user",
            password="TestPassword123"
        )

    def test_redactor_list_public(self):
        response = self.client.get(REDACTOR_LIST_VIEW_URL)
        self.assertNotEquals(
            response.status_code,
            200,
            msg="unauthenticated users mustn't have access to redactor_list page"
        )
        self.assertRedirects(
            response,
            reverse_lazy("login") + f"?next={REDACTOR_LIST_VIEW_URL}"
        )

    def test_redactor_create_view_public(self):
        response = self.client.get(REDACTOR_CREATE_VIEW_URL)
        self.assertNotEquals(
            response.status_code,
            200,
            msg="unauthenticated users mustn't have access to redactor_create page"
        )
        self.assertRedirects(
            response,
            reverse_lazy("login") + f"?next={REDACTOR_CREATE_VIEW_URL}"
        )

    def test_redactor_update_view_public(self):
        response = self.client.get(REDACTOR_UPDATE_VIEW_URL)
        self.assertNotEquals(
            response.status_code,
            200,
            msg="unauthenticated users mustn't have access to redactor_update page"
        )
        self.assertRedirects(
            response,
            reverse_lazy("login") + f"?next={REDACTOR_UPDATE_VIEW_URL}"
        )

    def test_redactor_detail_view_public(self):
        response = self.client.get(REDACTOR_DETAIL_VIEW_URL)
        self.assertNotEquals(
            response.status_code,
            200,
            msg="unauthenticated users mustn't have access to redactor_detail page"
        )
        self.assertRedirects(
            response,
            reverse_lazy("login") + f"?next={REDACTOR_DETAIL_VIEW_URL}"
        )

    def test_redactor_delete_view_public(self):
        response = self.client.get(REDACTOR_DELETE_VIEW_URL)
        self.assertNotEquals(
            response.status_code,
            200,
            msg="unauthenticated users mustn't have access to redactor_delete page"
        )
        self.assertRedirects(
            response,
            reverse_lazy("login") + f"?next={REDACTOR_DELETE_VIEW_URL}"
        )


class RedactorPrivate(TestCase):
    """
    class to create and login the user that is going to
    serve as a client for our tests.
    """

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="test_user",
            password="TestPassword123"
        )

    def setUp(self):
        self.client.force_login(self.user)


class RedactorListViewPrivateTests(RedactorPrivate):
    def test_redactor_list_view_private_access(self):
        response = self.client.get(REDACTOR_LIST_VIEW_URL)
        self.assertEqual(
            response.status_code,
            200
        )
