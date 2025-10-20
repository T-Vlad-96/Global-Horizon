from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Redactor(AbstractUser):
    years_of_experience = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(70),
        ],
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return f"redactors/{self.id}"

    class Meta:
        ordering = ("username",)



class Newspaper(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    publishers = models.ManyToManyField(Redactor, related_name="newspapers")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("title",)
