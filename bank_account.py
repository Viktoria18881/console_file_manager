def account():

    from os import path
    import json


    def add_money(account_data, summa):

        while not summa.isnumeric():
            input('Введите сумму : ')

        account_data['account'] += int(summa)
        print(f"'Сумма на вашем счете: {account_data['account']} ")
        return account_data

    def bue(account_data, summa):

        while not summa.isnumeric():
            summa = input('Введите сумму : ')

        summa = int(summa)

        if summa > account_data['account']:
            print('Недостаточно средств на счете!')
        else:
            account_data['account'] -= summa
            account_data[input('Введите название товара: ')] = summa

        return account_data

    def print_shopping_list(account_data):
        if len(account_data) > 1:
            print('История покупок:')
            for key, val in account_data.items():
                if key != 'account':
                    print(f'{key} --> {val} ')
        else:
            print('Список покупок пока пуст!')


    account_data = {
        'account': 0,
    }

    account_file_path = './account_data'
    if path.exists(account_file_path):
        with open(account_file_path, 'r', encoding='utf-8') as f:
            account_data = json.load(f)

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            account_data = add_money(account_data, input('Введите сумму для пополнения счета: '))
        elif choice == '2':
            account_data = bue(account_data, input('Введите сумму покупки: '))
        elif choice == '3':
            print_shopping_list(account_data)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

    with open(account_file_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(account_data))


if __name__ == '__main__':

    account()