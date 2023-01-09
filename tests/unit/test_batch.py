from models.orderline import OrderLine


def test_allocating_to_a_batch_reduces_available_quantity(batch, small_order) -> None:
    expected_batch_qty = 18
    batch.allocate(small_order)
    assert batch.available_qty == expected_batch_qty


def test_cannot_allocate_more_than_available_quantity(batch):
    large_order = OrderLine(orderid=23, sku='SMALL-TABLE', qty=25)
    assert batch.can_allocate(large_order) is False


def test_can_allocate_if_available_equal_to_required(batch):
    order_equal_to_available_qty = OrderLine(orderid=345, sku='SMALL-TABLE', qty=20)
    assert batch.can_allocate(order_equal_to_available_qty) is True


def test_cannot_allocate_orderline_to_batch_if_skus_not_identical(batch):
    different_sku_orderline = OrderLine(orderid=4567, sku='BIG-TABLE', qty=1)
    assert batch.can_allocate(different_sku_orderline) is False


def test_cannot_allocate_same_orderline_twice(batch, small_order):
    batch.allocate(small_order)
    assert batch.can_allocate(small_order) is False
