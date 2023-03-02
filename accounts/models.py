from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Foydalanuvchilar'
        verbose_name_plural = 'Foydalanuvchilar'
