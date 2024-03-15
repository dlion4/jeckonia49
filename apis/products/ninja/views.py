

from ninja import NinjaAPI, Schema, ModelSchema

from .schemas import  ProductVariantSchema
from apis.products.models import Product, ProductVariant

class ProductSchema(ModelSchema):
    class Meta:
        model = Product
        fields = ('id', 'name', 'image')


from typing import List

from ninja_extra import (
    api_controller, route,
    NinjaExtraAPI,
    http_get, http_post, http_put, http_delete, http_patch, http_generic
)

api = NinjaExtraAPI()
from ninja.constants import NOT_SET
@api_controller('products/', tags=['Product Actions'], auth=NOT_SET, permissions=[])
class ProductControllerApi:
    @http_get('', response=List[ProductSchema])
    def get_products(self):
        return Product.objects.all()
    
    @http_get('{product_pk}/', response=ProductSchema)
    def get_product(self, product_pk:int):
        return Product.objects.get(id=product_pk)

    
    
    @route.post('')
    def create_product(self, data:ProductSchema):
        # product = Product.objects.create(**data.dict())
        print("Received request data:", data)
        return {"data": 1}
    
        

    @http_put('{product_pk}/', response=ProductSchema)
    def update_product(self, payload: ProductSchema, product_pk):
        product = Product.objects.get(pk=product_pk)
        # proceed from here
        return product
    
    @http_delete('{product_pk}/', response=ProductSchema)
    def delete_product(self, product_pk):
        product = Product.objects.get(pk=product_pk)
        # proceed from here
        return product
    
    @http_patch('{product_pk}/', response=ProductSchema)
    def patch_product(self, payload: ProductSchema, product_pk):
        product = Product.objects.get(pk=product_pk)
        # proceed from here
        return product
    


@api_controller("{product_pk}/variants/", tags=['Product Variant Actions'], auth=NOT_SET, permissions=[])

class ProductVariantControllerApi:

    @http_get("", response=ProductVariantSchema)
    # return a single product
    def get_single_product(self, product_pk):
        return Product.objects.get(pk=product_pk)

    @http_get('', response=List[ProductVariantSchema])
    def get_product_variants(self, product_pk):
        product = self.get_single_product(product_pk)
        # proceed from here
        
        return product




api.register_controllers(ProductControllerApi)
api.register_controllers(ProductVariantControllerApi)