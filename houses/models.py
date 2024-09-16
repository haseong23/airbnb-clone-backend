from django.db import models

# Create your models here.
# DB에 접속하는 인터페이스라고 보면 될까?

class House(models.Model):
    """
    House model
    """
    # 속성
    name = models.CharField(max_length=140)
    price = models.PositiveBigIntegerField()
    discription = models.TextField()
    address = models.CharField(max_length=1500)