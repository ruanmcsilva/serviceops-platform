from rest_framework import serializers
from .models import Order, OrderService


class OrderServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderService
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    services = OrderServiceSerializer(
        source='orderservice_set',
        many=True,
        read_only=True
    )

    class Meta:
        model = Order
        fields = '__all__'