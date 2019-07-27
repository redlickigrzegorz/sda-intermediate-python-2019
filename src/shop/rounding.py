import decimal


def round_value(value, precision=2, rounding=decimal.ROUND_DOWN):
    exp = decimal.Decimal('10') ** -precision
    return value.quantize(exp, rounding=rounding)
