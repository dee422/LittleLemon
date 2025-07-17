from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from restaurant.models import Menu

class MenuViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=120, inventory=50)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
