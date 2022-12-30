import pytest

from batch import Batch
from orderline import OrderLine


@pytest.fixture
def order():
    return OrderLine(sku='SMALL-TABLE', qty=2)

@pytest.fixture
def batch():
    return Batch(reference='batch-001', sku='SMALL-TABLE', available_qty=20)
