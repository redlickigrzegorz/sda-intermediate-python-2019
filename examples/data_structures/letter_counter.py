from collections import defaultdict, Counter


def count_letters_v1(text: str) -> dict:
    counter = {}
    for letter in text:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    return counter


def count_letters_v2(text: str) -> dict:
    counter = defaultdict(int)
    for letter in text:
        counter[letter] += 1
    return counter


def count_letters_v3(text: str) -> Counter:
    return Counter(text)

if __name__ == '__main__':
    print("Example text")
    print(count_letters_v2("Example text"))
    print('*********************')
    #workers = {}
    #workers['developers'] = []
    workers = defaultdict(list)
    workers['developers'].append('Bob')
    print(workers)
    print('*********************')
    print(count_letters_v3('Ala Mmma kootTTaa'))
    print(count_letters_v3('Ala Mmma kootTTaa').most_common(4))
