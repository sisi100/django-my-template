from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class User(models.Model):
    name = models.CharField(verbose_name="名前", max_length=200)
    age = models.PositiveSmallIntegerField(
        verbose_name="年齢",
        validators=[MinValueValidator(0), MaxValueValidator(200)],
    )
