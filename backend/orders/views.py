from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import OrderSerializer
from .models import Order, OrderService
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.decorators import action

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    
    @action(detail=False, methods=['get'])
    def revenue(self, request):
        total = OrderService.objects.aggregate(revenue=Sum('total_price'))
        return Response(total)

    
    @action(detail=False, methods=['get'])
    def summary(self, request):
        data = {
            "total_orders": Order.objects.count(),
            "open_orders": Order.objects.filter(status="OPEN").count(),
            "total_revenue": OrderService.objects.aggregate(
                total=Sum("total_price")
            )["total"] or 0 
        }
        return Response(data)