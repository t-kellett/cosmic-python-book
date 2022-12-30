from orderline import OrderLine


def test_allocating_to_a_batch_reduces_available_quantity(batch, order) -> None:
    # arrange
    expected_batch_qty = 18
    # act
    batch.allocate(order)
    # assert
    assert batch.available_qty == expected_batch_qty


def test_cannot_allocate_more_than_available_quantity(batch, order):
    # arrange
    large_order = OrderLine(sku='SMALL-TABLE', qty=25)
    expected_batch_qty = 20
    # act
    batch.allocate(large_order)
    # assert
    assert batch.available_qty == expected_batch_qty


