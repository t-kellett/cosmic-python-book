from datetime import date
from typing import Optional

from models.orderline import OrderLine


class Batch:
    def __init__(self, reference: str, sku: str, available_qty: int, eta: Optional[date]) -> None:
        self.reference = reference
        self.sku = sku
        self.available_qty = available_qty
        self.allocations = set()
        self.eta = eta

    # special python method that defines the equality (==) behaviour for the class
    def __eq__(self, other):
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference

    # changing the hash of a batch instance to not be a random integer
    def __hash__(self):
        return hash(self.reference)

    # gt = greater than; use to set comparison for instances of this class so that the .sorted() method can be used
    def __gt__(self, other):
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta

    def allocate(self, order: OrderLine) -> None:
        if self.can_allocate(order):
            self.available_qty -= order.qty
            self.allocations.add(order)

    def can_allocate(self, order: OrderLine) -> bool:
        if order in self.allocations:
            return False
        return order.qty <= self.available_qty and self.sku == order.sku
