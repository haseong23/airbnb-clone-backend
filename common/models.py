from django.db import models


# Create your models here.
# 재사용만을 위한 모델임. 즉, DB화 하지 않는다.
class CommonModel(models.Model):
    """common model def"""

    created_at = models.DateTimeField(
        # obj 생성일시를 할당
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        # 매저장마다 할당
        auto_now=True,
    )

    class Meta:
        abstract = True
