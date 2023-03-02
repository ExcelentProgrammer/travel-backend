from django.urls import path
from .views import getMeAPIView

urlpatterns = [
    path("users/me/", getMeAPIView.as_view(), name='me'),
]
