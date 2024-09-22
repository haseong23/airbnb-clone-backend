from django.db import models
from common.models import CommonModel


class Experience(CommonModel):
    """경험 모델 정의"""

    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    name = models.CharField(max_length=250)
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()
    perks = models.ManyToManyField("experiences.Perk")

    def __str__(self) -> str:
        return self.name


class Perk(CommonModel):
    """경험 내 포함된 것들"""

    name = models.CharField(
        max_length=100,
    )
    details = models.CharField(max_length=250, blank=True, null=True, default="")
    explanation = models.TextField()

    def __str__(self) -> str:
        return self.name
