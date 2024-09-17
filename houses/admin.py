from django.contrib import admin
from .models import House

# Register your models here.
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    # 리스트형이거나 튜플형이어야함.
    # 인스턴스 선택전에 보여지는 컬럼
    list_display = (
        "name",
        "price_per_night",
        "address",
        "pets_allowed",
    )

    # 필터링
    list_filter = (
        "price_per_night",
        "pets_allowed",
    )

    # 검색
    search_fields = (
        "address__startswith",
        "name",
    )