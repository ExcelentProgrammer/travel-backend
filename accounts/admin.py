from django.contrib import admin
from .models import User
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import Group

class UserModelView(ModelAdmin):
    model = User
    list_display = ['username', "first_name", "phone"]


admin.site.unregister(Group)
admin.site.register(User, UserModelView)
