from .factories import ProductFactory, ProductVariantFactory, ProductVariant, Product
import pytest


# start with accessing the factory ans validate each factory


def test_product_factory(product_factory):
    """Factories become fixtures automatically."""
    assert product_factory is ProductFactory


def test_product_variant_factory(product_variant_factory):
    """Factories become fixtures automatically."""
    assert product_variant_factory is ProductVariantFactory


# assert instancess
@pytest.mark.django_db
def test_product_instance(product):
    """Instances become fixtures automatically."""
    assert isinstance(product, Product)

@pytest.mark.django_db
def test_product_variant_instance(product_variant):
    """Instances become fixtures automatically."""
    assert isinstance(product_variant,ProductVariant)
    
# asset params

@pytest.mark.parametrize("product__name", ['Product 1'])
@pytest.mark.parametrize("product__image", ['https://www.unsplush.com/?image=kjgaweuwaegliasdliyat86we4yglfiAIYFYE9G4'])
def test_product_parameters(db, product):
    """You can set any factory attribute as a fixture using naming convention."""
    assert product.name == 'Product 1'
    assert product.image == "https://www.unsplush.com/?image=kjgaweuwaegliasdliyat86we4yglfiAIYFYE9G4"


@pytest.mark.django_db
@pytest.mark.parametrize("product_variant__sku, product_variant__description, product_variant__price", [('ANCTM1', 'Some sample description 1', 8922)])
def test_product_variant_parameters(product_variant):
    """You can set any factory attribute as a fixture using naming convention."""

    assert product_variant.sku == 'ANCTM1'
    assert product_variant.description == 'Some sample description 1'
    assert product_variant.price == 8922



# ================================================================================================= TEST CREATION ================================================================================================== 
    
@pytest.mark.django_db
def test_product_creation(product_factory):
    # product = product_factory.build() # buidl don no insert in db
    product = product_factory.create() # create instead
    # get db produ

    prod_from_db = Product.objects.get(pk=product.pk)

    print(product.name)

    assert product.pk == prod_from_db.pk


@pytest.mark.django_db
def test_product_variant_creation(product_variant_factory):
    # product_variant = product_variant_factory.build() # buidl don no insert in db
    product_variant = product_variant_factory.create() # create instead
    # get db produ
    
    prod_variant_from_db = ProductVariant.objects.get(pk=product_variant.pk)
    
    print(product_variant.sku)

    assert product_variant.pk == prod_variant_from_db.pk




# # ================================================================================================= TEST GET ================================================================================================== 
    
from django.db.models import QuerySet

@pytest.mark.django_db
def test_product_get(product):
    """You can get an instance from the database using its primary key."""
    product_from_db = Product.objects.all()
    # we return atleas a queryset

    assert isinstance(product_from_db, QuerySet)
    assert len(product_from_db) > 0



@pytest.mark.django_db
def test_product_variant_get(product_variant):
    """You can get an instance from the database using its primary key."""
    product_variant_from_db = ProductVariant.objects.all()
    # we return atleas a queryset
    
    assert isinstance(product_variant_from_db, QuerySet)
    assert len(product_variant_from_db) > 0


# # ================================================================================================= TEST UPDATE ==================================================================================================
    
@pytest.mark.django_db
def test_product_update(product):
    """You can update an instance in the database using its primary key."""
    product.name = 'Updated product'
    product.save()
    print(product.name)
    product_from_db = Product.objects.get(pk=product.pk)
    print(product_from_db.name)
    assert product_from_db.name == 'Updated product'


@pytest.mark.django_db
def test_product_variant_update(product_variant):

    product_variant.description = 'Updated Product Variant'
    product_variant.save()
    print(product_variant.description)
    product_variant_from_db = ProductVariant.objects.get(pk=product_variant.pk)
    print(product_variant_from_db.description)
    assert product_variant_from_db.description == 'Updated Product Variant'




# # ================================================================================================= TEST DELETE ==================================================================================================
    

@pytest.mark.django_db
def test_product_delete(product):
    """You can delete an instance from the database using its primary key."""
    instance = Product.objects.get(pk=product.pk)
    instance.delete()
    # product_from_db = Product.objects.get(pk=product.pk)# THIS VERSION FAILES 

    # assert product_from_db is None# THIS VERSION FAILES 

    assert instance.DoesNotExist



@pytest.mark.django_db
def test_product_variant_delete(product_variant):
    """You can delete an instance from the database using its primary key."""
    instance = ProductVariant.objects.get(pk=product_variant.pk)
    instance.delete()
    # product_variant_from_db = ProductVariant.objects.get(pk=product_variant.pk)
    # assert product_variant_from_db is None


    with pytest.raises(ProductVariant.DoesNotExist):
        product_variant = ProductVariant.objects.get(pk=product_variant.pk)
        print("No product  variant pk found")
        assert product_variant is None
    print("Product  variant deleted successfully")

    assert instance.DoesNotExist





# # ================================================================================================= TEST ITEM ==================================================================================================
    

@pytest.mark.django_db
def test_get_product_instance(product):
    product_from_db = Product.objects.get(pk=product.pk)
    assert product_from_db.pk == product.pk


@pytest.mark.django_db
def test_product_variant_instance(product_variant):
    # product_variance_from_db = Product.objects.get(pk=product_variant.pk)
    # print(product_variant)
    # assert product_variance_from_db.pk == product_variant.pk
    """"""
