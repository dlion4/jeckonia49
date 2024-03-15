# from rest_framework import
from rest_framework import generics, status
from rest_framework.response import Response

from .mixins import ProductVariantApiViewMixin, ProductApiViewMixin

# ---------------------
# ================================== product  Api Views ==============================

class ProductListApiView(ProductApiViewMixin, generics.ListCreateAPIView):
    pass

class ProductDetailApiView(ProductApiViewMixin, generics.RetrieveAPIView):
    pass

class ProductDestroyApiView(ProductApiViewMixin, generics.DestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Product name %s , deleted successfuly" % instance.name},
            status=status.HTTP_204_NO_CONTENT,
            )
    

class ProductUpdateApiView(ProductApiViewMixin, generics.UpdateAPIView):
    pass


# ---------------------
# ================================== product Variant Api Views ==============================

class ProductVariantDetailApiView(ProductVariantApiViewMixin, generics.RetrieveAPIView):
    pass

class ProductVariantUpdateApiView(ProductVariantApiViewMixin, generics.UpdateAPIView):
    pass

class ProductVariantDestroyApiView(ProductVariantApiViewMixin, generics.DestroyAPIView):
    pass






