from ninja_extra import schemas

from ninja_schema import ModelSchema, model_validator
from apis.products.models import Product, ProductVariant

class ProductSchema(ModelSchema):
    class Config:
        model = Product
        
        

class ProductVariantSchema(ModelSchema):
    class Config:
        model = ProductVariant
        exclude = ("product",)
        

