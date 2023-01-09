from dataclasses import dataclass


@dataclass(frozen=True)
class OrderLine:
    orderid: int
    sku: str
    qty: int
