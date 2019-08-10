if __name__ == '__main__':
    with open('new_file.txt', 'r') as file:
        print(file.read(3))
        print(file.tell())
        print(file.read(3))
        print(file.seek(2))
        print(file.read(3))
    print('##############')

    with open('new_file.txt', 'r') as file:
        print(file.readline())
    print('##############')

    with open('new_file.txt', 'r') as file:
        for line in file.readlines():
            print(line)
    print('##############')

    with open('new_file.txt', 'r') as file:
        for line in file:
            print(line)
