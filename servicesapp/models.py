from django.db import models


# Create your models here.
class ServicesModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to="services/", default="services/default.jpg")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Xizmatlar'
        verbose_name_plural = 'Xizmatlar'
