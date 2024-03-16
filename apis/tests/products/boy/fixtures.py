import pytest
from rest_framework.test import APIClient

@pytest.fixture(scope="package")
def rest_api_client_endpoint():
    return APIClient()

