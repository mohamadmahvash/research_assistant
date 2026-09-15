from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, UserRegisterSerializer, ChangePasswordSerializer
from .services import create_user, change_password


class UserRegisterView(APIView):

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user(username=serializer.validated_data['username'], email=serializer.validated_data['email'],
                           password=serializer.validated_data['password'])
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)


class UserChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        change_password(user=request.user, new_password=serializer.validated_data["new_password"])
        return Response({"message": "Password change successfully"})
