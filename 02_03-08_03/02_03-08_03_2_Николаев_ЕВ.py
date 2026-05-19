print('Виртуальный счётчик зарплаты!')
summa_itog = 1
summa = 1
try:
    days = int(input('Введите количетсво дней: '))
except ValueError:
    print('Введите число!')
    exit()
for i in range(days):
    print(i + 1, 'день:', summa_itog, 'копеек')
    summa *= 2
    summa_itog += summa

print('Сумма до налогового вычета:', summa_itog / 200, 'рублей')

summa_nal = (summa_itog / 200) - (((summa_itog / 200) / 100) * 13)

print('Сумма после налогового вычета:', summa_nal, 'рублей')
