from django.urls import path
from .views import *

urlpatterns = [
    path('item/<int:id>/', item_page),
    path('buy/<int:id>/', buy_item),
    path('buy-order/<int:id>/', buy_order),
    path('buy-intent/<int:id>/', buy_intent),
    path('success/', success_page),
    path('cancel/', cancel_page),
]
