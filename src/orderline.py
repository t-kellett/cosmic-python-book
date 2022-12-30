from dataclasses import dataclass


@dataclass(frozen=True)
class OrderLine:
    sku: str
    qty: int