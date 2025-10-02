from django.db import IntegrityError
from django.test import TestCase

from newspapers_tracker.models import (
    Topic,
    Redactor,
    Newspaper
)


class TopicModelTests(TestCase):
    def test_topic_name_is_unique(self):
        topic = Topic.objects.create(name="test_name")
        with self.assertRaises(IntegrityError):
            Topic.objects.create(name="test_name")