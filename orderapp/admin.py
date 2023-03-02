from django.contrib import admin
from .models import OrderModel
from django.contrib.admin import ModelAdmin


class OrderAdminView(ModelAdmin):
    list_display = ['first_name',"phone","payment_type","addres","gmail","birth_day","user_count","is_pay"]
    model = OrderModel


admin.site.register(OrderModel,OrderAdminView)