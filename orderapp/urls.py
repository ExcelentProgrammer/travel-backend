from django.urls import path
from .views import OrderCreateAPIView,OrderDeleteAPIView,OrderGetAPIView,OrderAllAPIView

app_name = "order"

urlpatterns = [
    path("create/", OrderCreateAPIView.as_view(), name="create"),
    path("all/", OrderAllAPIView.as_view(), name="all"),
    path("delete/<int:id>", OrderDeleteAPIView.as_view(), name="delete"),
    path("get/<int:id>", OrderGetAPIView.as_view(), name="get"),
]
