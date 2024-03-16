from .fixtures import rest_api_client_endpoint
API_BASE_URL_ENDPOINT="/api/v1/drf/"
import pytest
from faker import Faker
from django.test import Client
from .factories import skuGen, Product

faker = Faker()


@pytest.fixture(scope="function")
def view_init():
    return Client()


@pytest.mark.django_db
def test_drf_get_endpoint_url_view(product, view_init):
    """Test the DRF GET endpoint URL view."""

    response = view_init.get(API_BASE_URL_ENDPOINT)
    
    assert response.status_code == 200
    print(response.json())
    assert response.json()
    # assert response.json()["message"] == "Hello World"



@pytest.mark.django_db
def test_obj_url(product, view_init):
    """Test the DRF GET endpoint URL view."""
    response = view_init.get(API_BASE_URL_ENDPOINT + str(product.id)+"/")
    
    assert response.status_code == 200
    print(response.json())
    assert response.json()
    # assert response.json()["message"] == "Hello World"


# @pytest.fixture

# def product():
#     # Create a product object using your Product model and return it
#     product = Product.objects.create(name=faker.name(), image=faker.url())  # Adjust attributes as needed
#     return product
from apis.products.restapi.serializers  import ProductSerializer
@pytest.mark.django_db

def test_drf_post_endpoint_url_view(product, view_init):
    """Test the DRF POST endpoint URL view."""
    # Create a serializer instance with data
    # Construct the POST data with product_variants included
    post_data = {
        "name": faker.name(),
        "image": faker.url(),
        "product_variants": [
            {
                "name": faker.name(),
                "sku": skuGen.sku_gen(),
                "price": faker.random_int(min=100, max=1000),
                "description": faker.text()
            } 
            for _ in range(3)
        ]
    }

    # Send a POST request with the serialized data
    response = view_init.post(API_BASE_URL_ENDPOINT, data=post_data)
    
    # Check the response
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    print(response.json())
    assert response.json(), "Response data is empty"


# @pytest.mark.django_db
def test_delete_product_view(db, product, view_init):
    # product_from_db = Product.objects.last()
    serializer_data = ProductSerializer(product).data
    print(serializer_data)
    response = view_init.delete(f"{API_BASE_URL_ENDPOINT}{str(product.pk)}/delete/", content_type="application/json")
    # assert response.status_code == 204, f"Expected status code 204, but got {response.status_code}"
    # print(response.json())
    assert response.status_code == 204, f"Expected status code 204, but got {response.status_code}"




@pytest.mark.django_db
def test_update_product_view(product, view_init):

    post_data = {
        "name": faker.name(),
        "image": faker.url(),
       
    }

    response = view_init.patch(f"{API_BASE_URL_ENDPOINT}{str(product.pk)}/update/", data=post_data, content_type="application/json")
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200



@pytest.mark.django_db
def test_put_product_view(product, view_init):
    post_data = {
        "name": faker.name(),
        "image": faker.url(),
       
    }
    response = view_init.put(f"{API_BASE_URL_ENDPOINT}{str(product.pk)}/update/", data=post_data, content_type="application/json")
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200