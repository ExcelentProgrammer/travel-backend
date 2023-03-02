from rest_framework.permissions import BasePermission
from .models import OrderModel


class IsMyOrder:
    def has_permission(self, request, view):
        order = OrderModel.objects.filter(id=view.kwargs['id'])
        if order.exists():
            if order.first().author == request.user:
                return True
            return False
        return False

    def has_object_permission(self, request, view, obj):
        return True
