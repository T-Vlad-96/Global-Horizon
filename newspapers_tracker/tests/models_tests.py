from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import IntegrityError
from django.test import TestCase

from newspapers_tracker.models import (
    Topic,
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
            "test_name",
            msg="__str__ method must return topic name"
        )

    def test_topic_ordering(self):
        self.assertEqual(
            self.topic._meta.ordering,
            ("name",),
            msg="topics must be ordered by 'name' field"
        )


class RedactorModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="test_username",
            first_name="test_first_name",
            last_name="test_last_name",
            password="TestPassword123",
            years_of_experience=25
        )

    def test_redactor_is_abstract_user_subclass(self):
        self.assertIsInstance(
            self.user,
            AbstractUser,
            msg=f"Redactor must be subclass of {AbstractUser}, not {type(self.user)}"
        )

    def test_redactor_str(self):
        self.assertEqual(
            str(self.user),
            "test_username",
            msg="Redactor __str__ method must return 'username' field value"
        )

    def test_redactor_ordering(self):
        self.assertEqual(
            self.user._meta.ordering,
            ("username",),
            msg="Redactor must be ordered by 'username' field"
        )

    def test_years_of_experience_field_exists(self):
        self.assertTrue(
            hasattr(self.user, "years_of_experience"),
            msg="Redactor must have 'years_of_experience' PositiveInteger field"
        )


class NewspaperModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.topic = Topic.objects.create(
            name="test_topic"
        )
        cls.publisher1 = get_user_model().objects.create_user(
            username="test_publisher1",
        )
        cls.publisher2 = get_user_model().objects.create_user(
            username="test_publisher2",
        )
        cls.newspaper = Newspaper.objects.create(
            title="test_title",
            content="test_content",
            topic=cls.topic
        )
        cls.newspaper.publishers.add(cls.publisher1)
        cls.newspaper.publishers.add(cls.publisher2)

    def test_newspaper_str(self):
        self.assertEqual(
            str(self.newspaper),
            "test_title",
            msg="Newspaper __str__ must return newspaper's title"
        )

    def test_newspaper_ordering(self):
        self.assertEqual(
            self.newspaper._meta.ordering,
            ("title",),
            msg="Newspaper must be ordered by 'title' field"
        )
