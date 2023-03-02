from django.urls import path
from .views import PaymeCreateAPIView,PaymeCheckAPIView

app_name = "paymeapp"

urlpatterns = [
    path('create/', PaymeCreateAPIView.as_view(), name="create"),
    path('check/<id>/', PaymeCheckAPIView.as_view(), name="check"),
]
