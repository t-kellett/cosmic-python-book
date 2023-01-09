from datetime import date
from typing import Optional

from models.orderline import OrderLine


class Batch:
    def __init__(self, reference: str, sku: str, available_qty: int, eta: Optional[date]) -> None:
        self.reference = reference
        self.sku = sku
        self.available_qty = available_qty
        self.allocations = dict()
        self.eta = eta

    def allocate(self, order: OrderLine) -> None:
        if self.can_allocate(order):
            self.available_qty -= order.qty
            self.allocations[order.id] = order

    def can_allocate(self, order: OrderLine) -> bool:
        if order.id in self.allocations:
            return False
        return order.qty <= self.available_qty and self.sku == order.sku
