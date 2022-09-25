from django.urls import path

from .views import (BuyView, CreatePaymentIntentOrderView, ItemView,
                    CheckoutView)


urlpatterns = [
    path('item/<int:pk>/', ItemView.as_view()),
    path('order/<int:pk>/', CreatePaymentIntentOrderView.as_view()),
    path('order_buy/<int:pk>/', CheckoutView.as_view()),
    path('buy/<int:pk>/', BuyView.as_view()),
]
