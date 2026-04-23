from django.urls import path
from .views import buy_item, item_page, success_page

urlpatterns = [
    path('buy/<int:id>/', buy_item),
    path('item/<int:id>/', item_page),
    path('success/', success_page),
]
