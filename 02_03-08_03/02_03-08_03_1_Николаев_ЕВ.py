string1 = input('Выберите валюту (рубли, доллары): ')
if string1 == 'рубли':
    print('Доступный номинал: 5 копеек, 10 копеек, 50 копеек')
    vvod = input('Введите монеты (через пробел): ')
    vvodn = vvod.split(' ')
    mon = []

    try:
        for x in vvodn:
            mon.append(int(x))
    except ValueError:
        print('Введён неверный номинал монеты')
        exit()


    if mon.count(5) + mon.count(10) + mon.count(50) != len(mon):
        print('Введён неверный номинал монеты')
        exit()

    k = 0
    for x in mon:
        k += x

    if k == 100:
        print('Поздравяем с выигрышем!')
    elif k < 100:
        print('Введенная сумма меньше рубля!')
    elif k > 100:
        print('Введенная сумма больше рубля!')



elif string1 == 'доллары':
    print('Доступный номинал: 1 цент, 5 центов, 10 центов, 25 центов')
    vvod = input('Введите монеты (через пробел): ')
    vvodn = vvod.split(' ')
    mon = []

    try:
        for x in vvodn:
            mon.append(int(x))
    except ValueError:
        print('Введён неверный номинал монеты')
        exit()

    if mon.count(1) + mon.count(5) + mon.count(10) + mon.count(25) != len(mon):
        print('Введён неверный номинал монеты')
        exit()

    k = 0
    for x in mon:
        k += x

    if k == 100:
        print('Поздравяем с выигрышем!')
    elif k < 100:
        print('Введенная сумма меньше доллара!')
    elif k > 100:
        print('Введенная сумма больше доллара!')


else:
    print('Введена неверная валюта!')
