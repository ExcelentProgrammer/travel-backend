from django.shortcuts import render
from .payme import Payme
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PaymeCreateSerializer
from drf_yasg.utils import swagger_auto_schema, status
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated
from orderapp.models import OrderModel
from servicesapp.models import ServicesModel

create_response_example = {
    status.HTTP_200_OK: openapi.Response(description="test", examples={
        'application/json': {
            'pay_url': 'https://checkout.paycom.uz/63f45590ca9e9f06ff959438',
            "pay_id": "63f45590ca9e9f06ff959438"
        }
    })
}
check_response_example = {
    status.HTTP_200_OK: openapi.Response(description="test", examples={
        'application/json': {
            'res': True,
        }
    })
}


class PaymeCreateAPIView(APIView):
    serializer_class = PaymeCreateSerializer

    def __init__(self, *args, **kwargs):
        self._payme = Payme()
        super().__init__(*args, **kwargs)

    @swagger_auto_schema(request_body=PaymeCreateSerializer, responses=create_response_example)
    def post(self, request):
        ser = PaymeCreateSerializer(data=request.data)

        if not ser.is_valid():
            return Response({"res": "not.confirmed"})

        service = ser.data.get("service")
        user_count = ser.data.get("user_count")

        amount = ServicesModel.objects.filter(id=service)

        if not amount.exists():
            return Response("service.not.found")
        else:
            amount = amount.first().price

        amount = int(amount) * int(user_count)

        res = self._payme.create(amount=amount)

        return Response(res)


class PaymeCheckAPIView(APIView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._payme = Payme()

    @swagger_auto_schema(responses=check_response_example)
    def get(self, request, id):
        return self.post(request, id)

    @swagger_auto_schema(responses=check_response_example)
    def post(self, request, id):
        res = self._payme.check(id)
        if res:
            OrderModel.objects.filter(pay_id=id).update(is_pay=True)
            print("to'lov qilindi")
        else:
            print("to'lov qilindi")

        return Response({"res": res})
