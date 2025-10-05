from django.test import TestCase
from django.urls import reverse_lazy

TOPIC_LIST_VIEW_URL = reverse_lazy("newspapers_tracker:topic-list")
TOPIC_CREATE_VIEW_URL = reverse_lazy("newspapers_tracker:topic-create")
TOPIC_UPDATE_VIEW_URL = reverse_lazy("newspapers_tracker:topic-update", pk=1)
TOPIC_DELETE_VIEW_URL = reverse_lazy("newspapers_tracker:topic-delete", pk=1)


class TopicViewsPublicTests(TestCase):
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
