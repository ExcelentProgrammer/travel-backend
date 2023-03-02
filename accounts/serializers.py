from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import User
from rest_framework import serializers


class CustomUserSerializer(UserSerializer):
    class Meta:
        fields = ['username', "password"]
        model = User


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta:
        fields = ['username', "first_name", "phone", "password"]
        model = User

class getMeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['first_name']
        model = User