
from .serializers import ProductSerializer, ProductVariantSerializer
from rest_framework import permissions

from apis.products.models import Product, ProductVariant



class ProductVariantApiViewMixin:
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer
    permission_classes = [permissions.AllowAny]
    lookup_url_kwarg = "slug"
    lookup_field = "slug"



class ProductApiViewMixin:
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    lookup_url_kwarg = "pk"
    lookup_field = "pk"
    
    