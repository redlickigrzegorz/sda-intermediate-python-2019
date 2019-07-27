from textwrap import wrap


def format_phone_number(number, area_code='+48', delimiter='-'):
    wrapped_number = delimiter.join(wrap(number, 3))
    return f'{area_code} (0) {wrapped_number}'


if __name__ == "__main__":
    print(format_phone_number('123456789', '+48', '-'))
    print(format_phone_number('123456789'))
    print(format_phone_number('123456789', '+66'))

    print(format_phone_number(area_code='+77', number='987654321'))
    print(format_phone_number(area_code='+77', number='987654321', delimiter=':'))

    print(format_phone_number('123123123', delimiter=' '))
    print(format_phone_number('111111111', delimiter=':', area_code='+12'))

    arguments = ("123456789", )
    print(format_phone_number(*arguments))
    keyword_arguments = {'number': '123456789','area_code': '+48', 'delimiter': '_' }
    print(format_phone_number(**keyword_arguments))
