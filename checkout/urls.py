from django.urls import path 
from checkout.views import  checkout_complete, create_payment
from checkout.webhook import strip_webhook

urlpatterns = [
    path('complete/', checkout_complete, name="checkout_complete"),
    path('create-payment-intent/<int:pk>/', create_payment, name='create-payment-intent'),
    path('stripe/webhook/', strip_webhook),
]


