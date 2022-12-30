from orderline import OrderLine


class Batch:
    def __init__(self, reference: str, sku: str, available_qty: int) -> None:
        self.reference = reference
        self.sku = sku
        self.available_qty = available_qty

    def allocate(self, order: OrderLine) -> None:
        if self.can_allocate(order):
            self.available_qty -= order.qty

    def can_allocate(self, order: OrderLine) -> bool:
        return order.qty <= self.available_qty