if __name__ == '__main__':
    file = open('new_file.txt', 'w')
    try:
        file.write('Ala ma kota.')
    finally:
        file.close()

    with open('new_file.txt', 'a') as file:
        file.write('\nKot ma Alę.')
