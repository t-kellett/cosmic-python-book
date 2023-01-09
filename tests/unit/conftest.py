from datetime import date

import pytest

from models.batch import Batch
from models.orderline import OrderLine


@pytest.fixture
def small_order():
    return OrderLine(id=1, sku='SMALL-TABLE', qty=2)

@pytest.fixture
def batch():
    return Batch(reference='batch-001', sku='SMALL-TABLE', available_qty=20, eta=date.today())
