import stripe
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Item, Order
from .services.stripe import create_checkout_session_for_item, create_checkout_session_for_order, create_payment_intent


def buy_item(request, id):
    item = get_object_or_404(Item, id=id)

    try:
        session = create_checkout_session_for_item(item)
        return JsonResponse({'session_id': session.id})

    except stripe.error.StripeError as e:
        return JsonResponse({'error': str(e)}, status=400)


def buy_order(request, id):
    order = get_object_or_404(Order, id=id)
    session = create_checkout_session_for_order(order)
    return JsonResponse({'session_id': session.id})


def buy_item_intent(request, id):
    item = get_object_or_404(Item, id=id)
    intent = create_payment_intent(item)
    return JsonResponse({'client_secret': intent.client_secret})


def item_page(request, id):
    item = get_object_or_404(Item, id=id)

    return render(request, 'item.html', {
        'item': item,
        'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY
    })


def success_page(request):
    return HttpResponse("Payment successful")


def cancel_page(request):
    return HttpResponse("Payment cancelled")


def home(request):
    return HttpResponse("Welcome")
