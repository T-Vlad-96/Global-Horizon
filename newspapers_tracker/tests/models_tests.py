from django.db import IntegrityError
from django.test import TestCase

from newspapers_tracker.models import (
    Topic,
    Redactor,
    Newspaper
)


class TopicModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.topic = Topic.objects.create(name="test_name")

    def test_topic_name_is_unique(self):
        with self.assertRaises(IntegrityError):
            Topic.objects.create(name="test_name")

    def test_topic_str_method(self):
        self.assertEqual(
            str(self.topic),
            "test_name"
        )

    def test_topic_ordering(self):
        self.assertEqual(
            self.topic._meta.ordering,
            ("name",)
        )
