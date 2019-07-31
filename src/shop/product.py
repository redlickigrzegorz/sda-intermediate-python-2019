from collections import namedtuple

Product = namedtuple("Product", ["name", "category", "price"])

tv = Product('tv', 'electronics', 1000)
iPhone = Product('iPhone', 'electronics', 500)
chocolate = Product('chocolate', 'food', 5)
