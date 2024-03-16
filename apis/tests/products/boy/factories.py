import factory

from apis.products.models import Product, ProductVariant

from faker import Factory as FakerFactory

import random
import string



faker = FakerFactory.create()


class SkuGenerator:

    
    def sku_gen(self):
        wide = 6
        ascii_sku_str = string.ascii_uppercase + string.digits
        sku = ''.join(random.choices(ascii_sku_str, k=wide))
        return sku
    

skuGen = SkuGenerator()

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.LazyFunction(lambda: faker.name())
    image = factory.LazyFunction(lambda: faker.url())


class ProductVariantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductVariant
    
    product = factory.SubFactory(ProductFactory)
    sku = factory.LazyFunction(lambda: skuGen.sku_gen())
    description = factory.LazyFunction(lambda: faker.text())
    price = factory.LazyFunction(lambda: faker.random_int(min=100, max=10000))



