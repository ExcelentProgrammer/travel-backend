from rest_framework import serializers


class PaymeCreateSerializer(serializers.Serializer):
    service = serializers.IntegerField()
    user_count = serializers.IntegerField(default=1)
