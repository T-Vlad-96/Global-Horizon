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
