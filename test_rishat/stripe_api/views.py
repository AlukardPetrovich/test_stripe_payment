import stripe

from django.shortcuts import render
from rest_framework.generics import (get_object_or_404, RetrieveAPIView,
                                     GenericAPIView)
from rest_framework.response import Response

from .models import Item, Order, OrderedItem
from .serializers import ItemSerializer, OrderSerializer
from test_rishat.settings import STRIPE_PRIVATE_KEY, STRIPE_PUBLISHABLE_KEY

stripe.api_key = STRIPE_PRIVATE_KEY


def calculate_order_amount(id):
    total_amount = 0
    order = get_object_or_404(Order, id=id)
    order_list = OrderedItem.objects.filter(order=order)
    for item in order_list:
        total_amount += item.item.price * item.amount
    return total_amount


class ItemView(RetrieveAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Item, id=kwargs['pk'])
        context = {
            'item': item,
            'stripe_pub_key': STRIPE_PUBLISHABLE_KEY
            }
        return render(request, 'quick_buy.html', context)


class BuyView(RetrieveAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Item, id=kwargs['pk'])
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/success.html',
            cancel_url='http://localhost:8000/cancel.html',
        )
        return Response({'id': session.id})


class CreatePaymentIntentOrderView(RetrieveAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def post(self, request, *args, **kwargs):
        intent = stripe.PaymentIntent.create(
            amount=calculate_order_amount(kwargs['pk']),
            currency='usd',
            automatic_payment_methods={
                'enabled': True,
            },
        )
        return Response({
            'clientSecret': intent['client_secret']
        })


class CheckoutView(GenericAPIView):

    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get(self, request, *args, **kwargs):
        items = OrderedItem.objects.filter(
            order=kwargs['pk']
            ).order_by('item__name')
        context = {
            'order_id': kwargs['pk'],
            'stripe_pub_key': STRIPE_PUBLISHABLE_KEY,
            'items': items
            }
        return render(request, 'order_buy.html', context)
