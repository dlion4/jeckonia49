from rest_framework import serializers, reverse
from apis.products.models import Product, ProductVariant
from django.utils.text import slugify

class ProductVariantSerializer(serializers.ModelSerializer):
    """
    A serializer for the ProductVariant model.
    """
    id = serializers.IntegerField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    variant_url = serializers.SerializerMethodField()
    update_url = serializers.SerializerMethodField()
    delete_url = serializers.SerializerMethodField()

    
    
    class Meta:
        model = ProductVariant
        fields = ['id',"sku", 'name', "slug", 'description', 'price', 'variant_url', 'update_url', 'delete_url']

    def create(self, validated_data):
        slug_data = validated_data.pop("sku", "test")
        variant = ProductVariant.objects.create(**validated_data)
        variant.slug = slugify(slug_data)
        variant.save()
        return variant
    


    def _variant_url(self, obj, path:str=""):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse.reverse(path, kwargs={
            "pk": obj.product.pk,
            "slug":obj.slug
            }, request=request)
    
    def get_variant_url(self, obj, path:str="product_variant_detail"):
        return self._variant_url(obj, path)

    
    def get_update_url(self, obj,path:str="product_variant_update"):
        return self._variant_url(obj, path)
    

    def get_delete_url(self, obj,path:str="product_variant_delete"):
        return self._variant_url(obj, path)

        

class ProductSerializer(serializers.ModelSerializer):
    """
    A serializer for the Product model.
    """
    id = serializers.IntegerField(read_only=True)
    product_variants = ProductVariantSerializer(many=True)

    obj_url = serializers.SerializerMethodField()
    update_url = serializers.SerializerMethodField()
    delete_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'obj_url','update_url','delete_url', "product_variants"]

    def get_product_variants(self, obj):
        """
        Custom method to serialize related ProductVariant instances.
        """
        variants = obj.product_variants.all()  # Assuming 'productvariant_set' is the related name
        return ProductVariantSerializer(variants, many=True).data
    
    def _obj_url(self, obj, path:str=""):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse.reverse(path, kwargs={"pk": obj.pk}, request=request)
    
    def get_obj_url(self, obj, path="product_detail"):
        return self._obj_url(obj, path)
    
    def get_update_url(self, obj, path="product_update"):
        return self._obj_url(obj, path)
    
    def get_delete_url(self, obj, path="product_delete"):
        return self._obj_url(obj, path)


    def create(self, validated_data):
        variants_data = validated_data.pop('product_variants', [])
        product = Product.objects.create(**validated_data)
        for variant_data in variants_data:
            variant = ProductVariant.objects.create(product=product, **variant_data)
            variant.slug = slugify(variant.sku)
            variant.save()
        print(variant_data)
        return product
    


