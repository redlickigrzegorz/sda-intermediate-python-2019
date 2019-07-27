from textwrap import wrap


def format_phone_number(number, area_code='+48', delimiter='-'):
    wrapped_number = delimiter.join(wrap(number, 3))
    return f'{area_code} (0) {wrapped_number}'


if __name__ == "__main__":
    print(format_phone_number('123456789', '+48', '-'))
    print(format_phone_number('123456789'))
    print(format_phone_number('123456789', '+66'))

