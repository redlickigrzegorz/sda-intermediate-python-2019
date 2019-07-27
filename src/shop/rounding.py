import decimal


def round_value(value, precision=2, rounding=decimal.ROUND_DOWN):
    exp = decimal.Decimal('10') ** -precision
    return value.quantize(exp, rounding=rounding)


#if __name__ == '__main__':
  #  print(round_value(decimal.Decimal('2.345'), 2, decimal.ROUND_UP))
   # print(round_value(decimal.Decimal('2.455')))
  #  print(round_value(decimal.Decimal('2.563'), rounding=decimal.ROUND_DOWN))
