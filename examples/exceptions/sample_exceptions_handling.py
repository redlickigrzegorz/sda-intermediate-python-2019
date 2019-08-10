if __name__ == '__main__':
    while True:
        text = input('Podaj mi liczbę: ')
        # if text.isdigit():
        # if isinstance(int(text), int):
        try:
            input_number = int(text)
        except (ValueError, TypeError) as error:
            print(f'Podałeś złą liczbę, a mówi o tym wyjątek:{error} ')
        except KeyError:
            print('Try again')
        # except Exception:
        #     pass
        else:
            print(f'Podałeś mi liczbę: {input_number}')
        finally:
            print('Spróbujmy jeszcze raz')
