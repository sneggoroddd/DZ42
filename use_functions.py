while True:
    print("1. пополнение счета")
    print("2. покупка")
    print("3. итория покупок")
    print("4. выход")
    print("5. Баланс")

    choice = input('Выбери пункт меню:')
    if choice == '1':
        balance = int(input('введите сумму пополнения баланса:'))
    elif choice == '2':
        pokupka = int(input('введите сумму покупки:'))
        balance = balance - pokupka
        if balance < 0:
            print('Недостаточно средств')
            balance = balance + pokupka
        else:
            balance = balance - pokupka
    elif choice == '3':
        pass
    elif choice == '4':
        break
    elif choice == '5':
        print("Ваш баланс:", balance)
    else:
        print("неверный пункт меню")