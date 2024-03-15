from django.urls import path, include

from rest_framework import routers
from .views import  ProductUpdateApiView, ProductDetailApiView, ProductUpdateApiView, ProductVariantDetailApiView, ProductVariantUpdateApiView, ProductVariantDestroyApiView, ProductListApiView, ProductDestroyApiView


urlpatterns = [
    path("", ProductListApiView.as_view(), name="product_list"),
    path("<pk>/", ProductDetailApiView.as_view(), name="product_detail"),
    path("<pk>/update/", ProductUpdateApiView.as_view(), name="product_update"),
    path("<pk>/delete/", ProductDestroyApiView.as_view(), name="product_delete"),
    path("<pk>/variants/<slug>/", ProductVariantDetailApiView.as_view(), name="product_variant_detail"),
    path("<pk>/variants/<slug>/delete/", ProductVariantDestroyApiView.as_view(), name="product_variant_delete"),
    path("<pk>/variants/<slug>/update/", ProductVariantUpdateApiView.as_view(), name="product_variant_update"),
]
