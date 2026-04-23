from django.test import TestCase
from unittest.mock import patch

from .models import Item, Order


class PaymentTestCase(TestCase):

    def setUp(self):
        self.item = Item.objects.create(name="Test item", description="Test description", price=77)

        self.order = Order.objects.create()
        self.order.items.add(self.item)

    def test_item_page(self):
        response = self.client.get(f'/item/{self.item.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.item.name)

    @patch('payment.views.create_checkout_session')
    def test_buy_item(self, mock_session):
        mock_session.return_value.id = "test_session"

        response = self.client.get(f'/buy/{self.item.id}/')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"id": "test_session"})

    @patch('payment.views.create_order_session')
    def test_buy_order(self, mock_session):
        mock_session.return_value.id = "order_session"

        response = self.client.get(f'/buy-order/{self.order.id}/')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"id": "order_session"})

    @patch('payment.views.create_payment_intent')
    def test_payment_intent(self, mock_intent):
        mock_intent.return_value.client_secret = "secret_777"

        response = self.client.get(f'/buy-intent/{self.item.id}/')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"client_secret": "secret_777"})

    def test_not_found(self):
        response = self.client.get('/item/777/')
        self.assertEqual(response.status_code, 404)
