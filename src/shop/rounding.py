import decimal


def round_value(value: decimal.Decimal, precision: int = 2, rounding: str = decimal.ROUND_DOWN) -> decimal.Decimal:
    exp = decimal.Decimal("10") ** -precision
    return value.quantize(exp, rounding=rounding)
