import decimal
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    category: str
    price: decimal.Decimal


game = Product("The Witcher III", "PS4 games", decimal.Decimal("199.90"))
headphones = Product("Bose QuietComfort 35 II", "headphones", decimal.Decimal("1299.00"))
computer = Product("Apple MacBook Air 2018", "notebook computer", decimal.Decimal("4999.00"))
