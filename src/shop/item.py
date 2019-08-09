from dataclasses import dataclass, field

from src.shop.product import Product


@dataclass
class Item:
    product: Product
    quantity: int = field(default=1)
