from string import ascii_uppercase, digits
from random import choices
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from restapi.models import Book


class BookTests(APITestCase):
    random_isbn = ''.join(choices(ascii_uppercase + digits, k=10))

    def test_create_book(self):
        """
        Ensure we can create a new book object.
        """
        old_count = Book.objects.count()
        url = reverse('books')
        data = {'title': 'API Book',
                'author': 'API',
                'isbn': BookTests.random_isbn,
                'price': '3.50',
                'description': 'automated'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), (old_count + 1))

    def test_create_book_unique_constraint(self):
        """
        Ensure we can't create a new book object with the same ISBN twice.
        """
        url = reverse('books')
        data = {'title': 'API Book',
                'author': 'API',
                'isbn': BookTests.random_isbn,
                'price': '3.50',
                'description': 'automated'}
        self.client.post(url, data, format='json')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
