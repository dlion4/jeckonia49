from apis.products.models import Product, ProductVariant

#create a fixture to prepopulate the data
import faker
fake = faker.Faker()

import pytest


# flow

# -- Arrange
# # -- Act
# # -- Assert

# def generate_faker_sku():
#     pass



# @pytest.fixture(scope="session")
# def product_setup():
#     """
#     This fixture is used to prepopulate the database
#     """
#     #create a product
#     product = Product.objects.create(
#         name="Product 1",
#         image="https://images.unsplash.com/photo-1624555130581-1d9cca783bc0?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8dXJsfGVufDB8fDB8fHww"
#     )

#     #create a product variant
#     variant = ProductVariant.objects.create(
#         product=product,
#         sku="123456789",
#         price=100,
#         description="This is a product variant"
#     )

# @pytest.mark.django_db
# def test_create_product():
#     prod = Product.objects.create(name="Prod 1")
#     assert prod.pk == 1
