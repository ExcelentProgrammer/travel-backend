from django.db import models
from accounts.models import User
from servicesapp.models import ServicesModel


class OrderModel(models.Model):
    # service

    GENDER_1 = "Erkak"
    GENDER_2 = "Ayol"

    genders = (
        (GENDER_1, "Erkak"),
        (GENDER_2, "Ayol")
    )

    PAYMENT_1 = "Naqd"
    PAYMENT_2 = "Payme"

    payment_choice = (
        (PAYMENT_1, "Naqd"),
        (PAYMENT_2, "Payme")
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    service = models.ForeignKey(ServicesModel, on_delete=models.CASCADE, related_name="service")
    user_count = models.IntegerField(default=1)
    payment_type = models.CharField(choices=payment_choice, default=PAYMENT_1, max_length=255)
    # end service

    # user
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    addres = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    gmail = models.CharField(max_length=255, blank=True, null=True)
    birth_day = models.DateField()
    gender = models.CharField(choices=genders, default=GENDER_1, max_length=255)
    is_pay = models.BooleanField(default=False)
    pay_id = models.CharField(max_length=255, blank=True, null=True)

    # end user

    def __str__(self):
        return f"{self.first_name}|{self.payment_type}|{self.gender}|{self.service.name}|{self.phone}|{self.is_pay}"

    class Meta:
        verbose_name = 'Buyurtmalar'
        verbose_name_plural = 'Buyurtmalar'