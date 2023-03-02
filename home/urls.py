from django.urls import path
from .views import HomePageAPIView

urlpatterns = [
    path("", HomePageAPIView.as_view(), name="home"),
]
