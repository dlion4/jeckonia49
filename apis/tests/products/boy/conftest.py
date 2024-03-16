import pytest

from pytest_factoryboy import register


from . import factories


register(factories.ProductFactory)
register(factories.ProductVariantFactory)