from dataclasses import dataclass


@dataclass(frozen=True)
class OrderLine:
    id: int
    sku: str
    qty: int
