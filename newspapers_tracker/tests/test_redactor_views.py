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
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        for i in range(7):
            get_user_model().objects.create_user(
                username=f"user_{i}",
                password="Abc12345"
            )

    def test_redactor_list_view_private_access(self):
        response = self.client.get(REDACTOR_LIST_VIEW_URL)
        self.assertEqual(
            response.status_code,
            200
        )

    def test_redactor_list_is_paginated_by_5(self):
        response = self.client.get(REDACTOR_LIST_VIEW_URL)
        self.assertEqual(
            len(response.context["redactor_list"]),
            5
        )

    def test_num_of_instances_on_second_page(self):
        # 8 redactor instance in general.
        # second page must have 3 instances if paginated_by = 5
        response = self.client.get(REDACTOR_LIST_VIEW_URL + "?page=2")
        self.assertEqual(
            response.status_code,
            200
        )
        self.assertEqual(
            len(response.context["redactor_list"]),
            3
        )

    def test_search_form_in_context(self):
        response = self.client.get(REDACTOR_LIST_VIEW_URL)
        self.assertIn(
            "search_form",
            response.context
        )

    def test_searching(self):
        response = self.client.get(
            REDACTOR_LIST_VIEW_URL,
            {"username": "1"}
        )
        self.assertEqual(
            len(response.context["redactor_list"]),
            1
        )
        self.assertEqual(
            response.context["redactor_list"][0].username,
            "user_1"
        )

    def test_empty_search(self):
        response = self.client.get(
            REDACTOR_LIST_VIEW_URL,
            {"username": ""}
        )
        self.assertEqual(
            len(response.context["redactor_list"]),
            5
        )


class RedactorCreateViewPrivateTests(RedactorPrivate):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.new_redactor_data = {
            "username": "new_user",
            "email": "test@gmail.com",
            "password1": "TestPassword123",
            "password2": "TestPassword123",
            "first_name": "new_user_first_name",
            "last_name": "new_user_last_name",
            "years_of_experience": 1
        }

    def test_redactor_create_view_access(self):
        response = self.client.get(REDACTOR_LIST_VIEW_URL)
        self.assertEqual(
            response.status_code,
            200
        )

    def test_redactor_create_view_creates_new_instance(self):
        self.assertEqual(
            len(get_user_model().objects.all()),
            1
        )
        response = self.client.post(
            REDACTOR_CREATE_VIEW_URL,
            self.new_redactor_data,
        )
        errors = ""
        if hasattr(response, "context") and response.context:
            errors = response.context["form"].errors.as_text()
        self.assertEqual(
            len(get_user_model().objects.all()),
            2,
            msg=f"{errors}"
        )

    def test_redactor_create_view_redirects(self):
        response = self.client.post(
            REDACTOR_CREATE_VIEW_URL,
            self.new_redactor_data,
        )
        self.assertRedirects(
            response,
            REDACTOR_LIST_VIEW_URL,
        )


class RedactorUpdateViewPrivateTests(RedactorPrivate):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.data_to_user_update = {
            "username": "user_updated",
            "email": "test@gmail.com",
            "first_name": "updated_first_name",
            "last_name": "updated_last_name",
            "years_of_experience": 2
        }

    def test_redactor_update_view_access(self):
        response = self.client.get(REDACTOR_UPDATE_VIEW_URL)
        self.assertEqual(
            response.status_code,
            200
        )

    def test_redactor_update_view_updates_an_instance(self):
        redactor_instance = get_user_model().objects.get(id=1)
        self.assertNotEquals(
            {
                "username": redactor_instance.username,
                "email": redactor_instance.email,
                "first_name": redactor_instance.first_name,
                "last_name": redactor_instance.last_name,
                "years_of_experience": redactor_instance.years_of_experience
            },
            self.data_to_user_update
        )
        response = self.client.post(
            REDACTOR_UPDATE_VIEW_URL,
            self.data_to_user_update
        )
        redactor_instance = get_user_model().objects.get(id=1)
        self.assertEqual(
            {
                "username": redactor_instance.username,
                "email": redactor_instance.email,
                "first_name": redactor_instance.first_name,
                "last_name": redactor_instance.last_name,
                "years_of_experience": redactor_instance.years_of_experience
            },
            self.data_to_user_update
        )

    def test_redactor_update_view_redirects(self):
        response = self.client.post(
            REDACTOR_UPDATE_VIEW_URL,
            self.data_to_user_update
        )
        self.assertRedirects(
            response,
            REDACTOR_LIST_VIEW_URL
        )


class RedactorDetailViewPrivateTests(RedactorPrivate):
    def test_redactor_detail_view_access(self):
        response = self.client.get(REDACTOR_DETAIL_VIEW_URL)
        self.assertEqual(
            response.status_code,
            200
        )

    def test_redactor_detail_view_template(self):
        response = self.client.get(REDACTOR_DETAIL_VIEW_URL)
        self.assertTemplateUsed(
            response,
            "newspapers_tracker/redactor_detail.html"
        )

