from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import getMeSerializer
from accounts.models import User


class getMeAPIView(APIView):

    def get(self, request):
        user = request.user
        user = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "phone": user.phone,
            "email": user.email
        }
        return Response(user)
