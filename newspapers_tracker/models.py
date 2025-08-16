from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(70),
        ]
    )

    def __str__(self):
        return self.username
