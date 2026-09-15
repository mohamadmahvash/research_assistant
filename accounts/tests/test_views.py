from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from accounts.models import User


class UserRegisterTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="mohamad",
            email="mohamad@test.com",
            password="123456"
        )

    def test_register_with_existing_email(self):
        url = reverse("accounts:register")
        data = {
            "username": "mohamad",
            "email": "mohamad@test.com",
            "password": "123456"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_can_register(self):
        url = reverse("accounts:register")
        data = {
            "username": "test6",
            "email": "test6@gmail.com",
            "password": "test6"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email="test6@gmail.com").exists())
