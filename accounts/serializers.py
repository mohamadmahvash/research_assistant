from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'date_joined']


class UserRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    # field-level validation
    def validate_email(self, value):
        user = User.objects.filter(email=value).exists()
        if user:
            raise serializers.ValidationError("Email already registered")
        return value

    def validate_username(self, value):
        if value == "admin":
            raise serializers.ValidationError("username can not be admin")
        return value


class ChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField()
