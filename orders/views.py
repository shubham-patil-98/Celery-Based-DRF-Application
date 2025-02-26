from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Prefetch
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from .decorators import customer_only

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return all products for both customers and sellers.
        """
        return Product.objects.all()

    def perform_create(self, serializer):
        """
        Allow only sellers to add products.
        """
        user = self.request.user
        if hasattr(user, 'seller'):
            serializer.save()
        else:
            raise PermissionDenied("Only sellers can add products.")

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Order, Product
from .serializers import OrderSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Customers see only their own orders.
        Sellers see all orders for their products.
        """
        user = self.request.user
        if hasattr(user, 'customer'):
            # Customers see only their orders
            return Order.objects.filter(customer__user=user)
        elif hasattr(user, 'seller'):
            # Sellers see orders for their products
            return Order.objects.filter(products__in=Product.objects.filter(seller=user.seller))
        elif user.is_superuser:
            # Superusers see all orders
            return Order.objects.all()
        return Order.objects.none()  # Deny access to unauthorized users

    def perform_create(self, serializer):
        """
        Customers can only place orders.
        """
        user = self.request.user
        if hasattr(user, 'customer'):
            serializer.save(customer=user.customer)
        else:
            raise PermissionDenied("Only customers can place orders.")


