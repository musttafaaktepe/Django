from rest_framework.test import APITestCase,APIRequestFactory
from django.contrib.auth.models import AnonymousUser

class FlightTestCase(APITestCase):

    def setUp(self):
        self.factory=APIRequestFactory()
    def test_flight_list_as_non_auth_user(self):
        request = self.factory.get()