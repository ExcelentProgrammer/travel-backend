from django.urls import path
from .views import getAllServices, oneServicesAPIView

urlpatterns = [
    path("all/", getAllServices.as_view(), name="all"),
    path("get/<int:id>", oneServicesAPIView.as_view(), name="one"),
]
