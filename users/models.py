from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):

    class GenderChoices(models.TextChoices):
        MALE = ("male", "남성")
        FEMALE = ("female", "여성")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "한국어")
        EN = ("en", "영어")

    class CurrencyChoices(models.TextChoices):
        WON = "won", "원화"
        USD = "usd", "달러"

    # Overwrite
    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )

    # custom
    avatar = models.ImageField(blank=True)
    name = models.CharField(
        max_length=150,
        default="",
    )
    is_host = models.BooleanField(default=False)
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    language = models.CharField(
        max_length=3,
        choices=LanguageChoices.choices,
    )
    currency = models.CharField(
        max_length=3,
        choices=CurrencyChoices.choices,
    )
