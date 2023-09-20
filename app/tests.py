from django.test import TestCase

from app.models import Book

# Create your tests here.

class TestBook(TestCase):
    def test_create_book(self):
        book = Book.objects.create(name="Hello", author="World")
        self.assertCountEqual(Book.objects.all(), [book])
