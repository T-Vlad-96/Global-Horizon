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
        cls.topic = Topic.objects.create(name="test_topic")
        cls.newspaper = Newspaper.objects.create(
            title="test_newspaper",
            topic=cls.topic
        )
        cls.newspaper.publishers.add(cls.user)

    def setUp(self):
        self.client.force_login(self.user)


class NewspaperListViewPrivateTests(NewspaperPrivate):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        for i in range(6):
            Newspaper.objects.create(
                title=f"newspaper_{i}",
                topic=cls.topic
            )

    def test_newspaper_list_view_access(self):
        response = self.client.get(NEWSPAPER_LIST_URL)
        self.assertEqual(
            response.status_code,
            200
        )

    def test_newspaper_list_is_paginated(self):
        response = self.client.get(NEWSPAPER_LIST_URL)
        self.assertTrue(
            response.context["is_paginated"],
            msg="newspaper_list must be paginated"
        )

    def test_newspaper_list_num_of_newspapers_on_page(self):
        response = self.client.get(NEWSPAPER_LIST_URL)
        self.assertEqual(
            len(response.context["newspaper_list"]),
            5,
            msg="newspaper_list must be paginated_by 5"
        )

    def test_newspaper_list_num_of_instances_on_second_page(self):
        response = self.client.get(NEWSPAPER_LIST_URL + "?page=2")
        # Total num of instances = 7, 2 must be on second page when paginated_by = 5
        self.assertEqual(
            len(response.context["newspaper_list"]),
            2,
            msg="num of instances on second page must be 2 if paginated_by = 5"
        )

    def test_newspaper_list_context_has_search_form(self):
        response = self.client.get(NEWSPAPER_LIST_URL)
        self.assertIn(
            "search_form",
            response.context
        )

    def test_searching_on_newspaper_list_page(self):
        response = self.client.get(NEWSPAPER_LIST_URL, {"title": "1"})
        self.assertEqual(
            len(response.context["newspaper_list"]),
            1
        )
        self.assertEqual(
            response.context["newspaper_list"][0].title,
            "newspaper_1"
        )

    def test_newspaper_list_empty_search_returns_full_list(self):
        response = self.client.get(NEWSPAPER_LIST_URL, {"title": ""})
        self.assertEqual(
            len(response.context["newspaper_list"]),
            5
        )

    def test_newspaper_list_uses_correct_template(self):
        response = self.client.get(NEWSPAPER_LIST_URL)
        self.assertTemplateUsed(
            response,
            "newspapers_tracker/newspaper_list.html"
        )


class NewspaperCreateViewPrivateTests(NewspaperPrivate):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.topic_1 = Topic.objects.create(name="test_topic_1")
        cls.new_newspaper_data = {
            "title": "added_newspaper",
            "topic": cls.topic.id,
            "content": "New content",
            "publishers": [cls.user.id]
        }

    def test_newspaper_create_access(self):
        response = self.client.get(NEWSPAPER_CREATE_URL)
        self.assertEqual(
            response.status_code,
            200
        )

    def test_newspaper_create_adds_new_instance(self):
        self.assertEqual(
            len(Newspaper.objects.all()),
            1
        )
        response = self.client.post(
            NEWSPAPER_CREATE_URL,
            self.new_newspaper_data
        )
        self.assertEqual(
            len(Newspaper.objects.all()),
            2
        )

    def test_newspaper_create_view_redirects(self):
        response = self.client.post(
            NEWSPAPER_CREATE_URL,
            self.new_newspaper_data
        )
        self.assertRedirects(
            response,
            NEWSPAPER_LIST_URL
        )

    def test_newspaper_create_view_uses_correct_template(self):
        response = self.client.get(NEWSPAPER_CREATE_URL)
        self.assertTemplateUsed(
            response,
            "newspapers_tracker/newspaper_form.html"
        )
