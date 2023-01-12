from datetime import date, timedelta

import pytest

from models.batch import Batch
from models.orderline import OrderLine


@pytest.fixture
def small_order():
    return OrderLine(orderid=1, sku='SMALL-TABLE', qty=2)


@pytest.fixture
def batch():
    return Batch(reference='batch-001', sku='SMALL-TABLE', available_qty=20, eta=date.today())


@pytest.fixture
def today():
    return date.today()


@pytest.fixture
def tomorrow(today):
    return today + timedelta(days=1)
