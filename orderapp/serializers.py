from rest_framework import serializers
from .models import OrderModel


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = [
            "id",
            "service",
            "user_count",
            "payment_type",
            "first_name",
            "last_name",
            "addres",
            "phone",
            "gmail",
            "birth_day",
            "gender",
            "pay_id",
        ]

