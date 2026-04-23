import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_checkout_session(item):
    return stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount': item.price * 100,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=f"{settings.DOMAIN}/success/",
        cancel_url=f"{settings.DOMAIN}/cancel/",
    )


def create_order_session(order):
    line_items = []

    for item in order.items.all():
        line_items.append({
            'price_data': {
                'currency': item.currency,
                'product_data': {'name': item.name},
                'unit_amount': item.price * 100,
            },
            'quantity': 1,
        })

    return stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=f"{settings.DOMAIN}/success/",
        cancel_url=f"{settings.DOMAIN}/cancel/",
    )


def create_payment_intent(item):
    return stripe.PaymentIntent.create(amount=item.price * 100, currency=item.currency)
