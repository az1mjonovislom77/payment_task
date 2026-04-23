from django.test import TestCase
from unittest.mock import patch
from .models import Item


class ItemTestCase(TestCase):

    def setUp(self):
        self.item = Item.objects.create(name="Test Item", description="Test Description", price=100)

    def test_item_page(self):
        response = self.client.get(f'/item/{self.item.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.item.name)

    @patch('payment.views.create_checkout_session')
    def test_buy_item(self, mock_create_session):
        mock_create_session.return_value.id = "test_session_id"

        response = self.client.get(f'/buy/{self.item.id}/')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'session_id': 'test_session_id'})

    def test_item_not_found(self):
        response = self.client.get('/item/999/')
        self.assertEqual(response.status_code, 404)
