from django.db import models


# Create your models here.
class Room(models.Model):
    """Room Model Definition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = "entired_place", "Entire place"
        PRIVATE_ROOM = "private_room", "Private room"
        SHARED_ROOM = "shared_room", "Shared room"

    country = models.CharField(max_length=50, defautl="한국")
    city = models.CharField(max_length=80, default="서울")
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    pet_friendly = models.BooleanField(default=False)
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )
    owner = models.ForeignKey("Users.user", on_delete=models.CASCADE)


class Amenity(models.Model):
    """Amenity Defition"""

    name = models.CharField(max_length=150)
    description = models.CharField(
        max_length=150,
        null=True,
    )
