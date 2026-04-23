from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Item
from .services import create_checkout_session


def buy_item(request, id):
    try:
        item = get_object_or_404(Item, id=id)
        session = create_checkout_session(item)
        return JsonResponse({'id': session.id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def item_page(request, id):
    item = get_object_or_404(Item, id=id)

    return render(request, 'item.html', {
        'item': item,
        'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY
    })


def success_page(request):
    return HttpResponse("Payment successful ✅")
