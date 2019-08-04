import re

if __name__ == '__main__':

    text1 = 'Ala ma kota'
    reg1 = r'([AU]la)\sma\s(.+)' # r - raw text
    match1 = re.search(reg1, text1)
    print(match1.groups())
    print(match1.group(1))
    print(match1.span())
    print(match1.string)

    print('********************')

    text2 = 'Moj numer telefonu to 123456789'
    reg2 = r'.*(\d{9}).*'
    match2 = re.match(reg2, text2)
    if match2:
        print(match2.group(1))

    print('*************************')

    text3 = 'Moj numer telefonu to 123456789 lub 987654321'
    reg3 = r'\d{9}'
    match3 = re.findall(reg3, text3)
    print(match3)

    print('*************')

    text4 = 'Ula ma kota i ma psa'
    reg4 = r'\sma\s'
    sub1 = re.sub(reg4, ' nie ma ', text4 )
    print(sub1)
    reg5 = r'ma kota'
    sub2 = re.sub(reg5, 'nie ma kota', text4)
    print(sub2)

    print('**********************')

    text5 = 'Tomek, Radek, Krzysiek'
    print(text5.split(', '))
    reg6 = r'\W{2}'
    print(re.split(reg6, text5))

    print('**********************')

    text7 = 'TomekRadekKrzysiek'
    reg7 = r'(?=[A-Z])'
    print(re.split(reg7, text7))
