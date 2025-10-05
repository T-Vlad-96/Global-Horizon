from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from newspapers_tracker.models import Topic

TOPIC_LIST_VIEW_URL = reverse_lazy("newspapers_tracker:topic-list")
TOPIC_CREATE_VIEW_URL = reverse_lazy("newspapers_tracker:topic-create")
TOPIC_UPDATE_VIEW_URL = reverse_lazy("newspapers_tracker:topic-update", kwargs={"pk": 1})
TOPIC_DELETE_VIEW_URL = reverse_lazy("newspapers_tracker:topic-delete", kwargs={"pk": 1})


class TopicViewsPublicTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.topic = Topic.objects.create(name="test_topic")

    def test_topic_list_view_public(self):
        response = self.client.get(TOPIC_LIST_VIEW_URL)
        self.assertNotEquals(
            response.status_code,
            200
        )
        self.assertRedirects(
            response,
            reverse_lazy("login") + "?next=/topics/"
        )

    def test_topic_create_view_public(self):
        response = self.client.get(TOPIC_CREATE_VIEW_URL)
        self.assertNotEquals(
            response.status_code,
            200
        )
        self.assertRedirects(
            response,
            reverse_lazy("login") + "?next=/topics/create/"
        )

    def test_topic_update_view_public(self):
        response = self.client.get(TOPIC_UPDATE_VIEW_URL)
        self.assertNotEquals(
            response.status_code,
            200
        )
        self.assertRedirects(
            response,
            reverse_lazy("login") + "?next=/topics/update/1/"
        )

    def test_topic_delete_view_public(self):
        response = self.client.get(TOPIC_DELETE_VIEW_URL)
        self.assertNotEquals(
            response.status_code,
            200
        )
        self.assertRedirects(
            response,
            reverse_lazy("login") + "?next=/topics/delete/1/"
        )


class TopicListViewPrivateTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(7):
            Topic.objects.create(name=f"topic_{i}")
        cls.user = get_user_model().objects.create_user(
            username="test_user",
            password="Abc12345"
        )

    def setUp(self):
        self.client.force_login(self.user)

    def test_topic_list_view_access(self):
        response = self.client.get(TOPIC_LIST_VIEW_URL)
        self.assertEqual(
            response.status_code,
            200
        )

    def test_topic_list_view_paginated_by_5(self):
        response = self.client.get(TOPIC_LIST_VIEW_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(
            len(response.context["topic_list"]),
            5
        )

    def test_topic_list_view_topics_num_on_second_page(self):
        response = self.client.get(TOPIC_LIST_VIEW_URL + "?page=2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(response.context["topic_list"]),
            2
        )

    def test_search_form_in_context(self):
        response = self.client.get(TOPIC_LIST_VIEW_URL)
        self.assertIn("search_form", response.context)

    def test_topic_list_view_searching(self):
        response = self.client.get(TOPIC_LIST_VIEW_URL + "?name=1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(response.context["topic_list"]),
            1
        )
        self.assertEqual(
            response.context["topic_list"][0].name,
            "topic_1"
        )

    def test_empty_search_returns_full_list(self):
        response = self.client.get(TOPIC_LIST_VIEW_URL + "?name= ")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(response.context["topic_list"]),
            5
        )


class TopicCreateViewPrivateTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="test_user",
            password="Abc12345"
        )
        cls.new_topic_data = {
            "name": "new_topic"
        }

    def setUp(self):
        self.client.force_login(self.user)

    def test_topic_create_view_access(self):
        response = self.client.get(TOPIC_CREATE_VIEW_URL)
        self.assertEqual(
            response.status_code,
            200
        )

    def test_topic_create_view_creates_new_instance(self):
        self.assertEqual(
            len(Topic.objects.all()),
            0
        )
        response = self.client.post(
            TOPIC_CREATE_VIEW_URL,
            self.new_topic_data
        )
        self.assertEqual(
            len(Topic.objects.all()),
            1
        )
        self.assertEqual(
            Topic.objects.get(id=1).name,
            "new_topic"
        )

    def test_topic_create_view_redirects(self):
        response = self.client.post(
            TOPIC_CREATE_VIEW_URL,
            self.new_topic_data
        )
        self.assertRedirects(
            response,
            TOPIC_LIST_VIEW_URL
        )
