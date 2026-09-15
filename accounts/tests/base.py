from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class BaseAPITestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.admin = User.objects.create_superuser(email="mahvash1@gmail.com", username="mahvash1", password="mahvash1")
        cls.user = User.objects.create_user(email="mahvash2@gmail.com", username="mahvash2", password="mahvash2")

    def login_user(self):
        self.client.force_authenticate(self.user)

    def login_admin(self):
        self.client.force_authenticate(self.admin)

    def logout(self):
        self.client.force_authenticate(user=None)
