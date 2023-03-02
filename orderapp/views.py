from django.shortcuts import render
from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveAPIView
from .serializers import OrderCreateSerializer
from rest_framework.views import APIView
from .models import OrderModel
from rest_framework.permissions import IsAuthenticated
from .permissions import IsMyOrder
from rest_framework.response import Response


class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderCreateSerializer
    model = OrderModel
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class OrderDeleteAPIView(DestroyAPIView):
    serializer_class = OrderCreateSerializer
    model = OrderModel
    permission_classes = [IsAuthenticated, IsMyOrder]
    lookup_field = "id"
    queryset = OrderModel.objects.all()

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        self.perform_destroy(obj)
        return Response({"res": "order.delete.success"})


class OrderGetAPIView(RetrieveAPIView):
    serializer_class = OrderCreateSerializer
    queryset = OrderModel.objects.all()
    permission_classes = [IsAuthenticated, IsMyOrder]
    lookup_field = "id"

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        data = self.get_serializer(obj).data
        id = data['id']
        is_pay = OrderModel.objects.filter(id=id).first().is_pay
        data['is_pay'] = is_pay
        return Response(data)


class OrderAllAPIView(APIView):

    def get(self,request):
        orders = OrderModel.objects.filter(author=request.user).values()
        return Response(orders)
