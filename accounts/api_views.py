from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, UserRegisterSerializer
from .services import *


class UserRegisterAPIView(APIView):

    @staticmethod
    def post(request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user(username=serializer.validated_data['username'], email=serializer.validated_data['email'],
                           password=serializer.validated_data['password'])
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)
