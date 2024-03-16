from apis.products.models import Product, ProductVariant
import pytest
 
from django.shortcuts import get_object_or_404

@pytest.fixture(scope="function")
def product_1(db):
    return Product.objects.create(name="Product 1" )


@pytest.mark.django_db
def test_create_product(product_1):
    prod = product_1

    assert prod.name == "Product 1"


@pytest.mark.django_db
def test_get_product(product_1):
    prod = Product.objects.get(pk=product_1.pk)
    print(prod)
    assert prod.name == "Product 1"



@pytest.mark.django_db
def test_delete_product(product_1):
    prod = Product.objects.get(pk=product_1.pk)
    prod.delete()
    
    with pytest.raises(Product.DoesNotExist) as ex:
        new_prod = (Product.objects.get(pk=product_1.pk))
        assert new_prod == None





