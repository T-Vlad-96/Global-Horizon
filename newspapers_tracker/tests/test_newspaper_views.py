from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from newspapers_tracker.models import Newspaper, Topic

NEWSPAPER_LIST_URL = reverse_lazy("newspapers_tracker:newspaper-list")
NEWSPAPER_CREATE_URL = reverse_lazy("newspapers_tracker:newspaper-create")
NEWSPAPER_DETAIL_URL = reverse_lazy(
    "newspapers_tracker:newspaper-detail",
    kwargs={"pk": 1}
)
NEWSPAPER_UPDATE_URL = reverse_lazy(
    "newspapers_tracker:newspaper-update",
    kwargs={"pk": 1}
)
NEWSPAPER_DELETE_URL = reverse_lazy(
    "newspapers_tracker:newspaper-delete",
    kwargs={"pk": 1}
)


class NewspaperViewsPublicTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.topic = Topic.objects.create(name="test_topic")
        cls.publisher = get_user_model().objects.create_user(
            username="test_username",
            password="Abc12345"
        )
        cls.newspaper = Newspaper.objects.create(
            title="test_title",
            topic=cls.topic,
        )
        cls.newspaper.publishers.add(cls.publisher)

    def test_newspaper_list_view_access_public(self):
        response = self.client.get(NEWSPAPER_LIST_URL)
        self.assertNotEquals(
            response.status_code,
            200,
            msg="Access for authenticated users only"
        )

    def test_newspaper_create_view_access_public(self):
        response = self.client.get(NEWSPAPER_CREATE_URL)
        self.assertNotEquals(
            response.status_code,
            200,
            msg="Access for authenticated users only"
        )

    def test_newspaper_detail_view_access_public(self):
        response = self.client.get(NEWSPAPER_DETAIL_URL)
        self.assertNotEquals(
            response.status_code,
            200,
            msg="Access for authenticated users only"
        )

    def test_newspaper_update_view_access_public(self):
        response = self.client.get(NEWSPAPER_UPDATE_URL)
        self.assertNotEquals(
            response.status_code,
            200,
            msg="Access for authenticated users only"
        )

    def test_newspaper_delete_view_access_public(self):
        response = self.client.get(NEWSPAPER_DELETE_URL)
        self.assertNotEquals(
            response.status_code,
            200,
            msg="Access for authenticated users only"
        )


class NewspaperPrivate(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="test_user",
            password="TestPassword123"
        )
        topic = Topic.objects.create(name="test_topic")
        newspaper = Newspaper.objects.create(
            title="test_newspaper",
            topic=topic
        )
        newspaper.publishers.add(cls.user)

    def setUp(self):
        self.client.force_login(self.user)
