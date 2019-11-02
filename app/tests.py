from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Adonator
from rest_framework import status
from rest_framework.test import APIClient

class AccountsTest(APITestCase):
    def setUp(self):
        # We want to go ahead and originally create a user. 
        self.test_user = Adonator.objects.create_user('testuser', 'test@example.com', 'testpassword')

        # URL for creating an account.
        self.client = APIClient()

    def test_create_user(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        data = {
            'username': 'foobar',
            'email': 'foobar@example.com',
            'password': 'somepassword'
        }

        response = self.client.post('register', data, format='json')

        # We want to make sure we have two users in the database..
        self.assertEqual(Adonator.objects.count(), 2)
        # And that we're returning a 201 created code.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Additionally, we want to return the username and email upon successful creation.
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)
