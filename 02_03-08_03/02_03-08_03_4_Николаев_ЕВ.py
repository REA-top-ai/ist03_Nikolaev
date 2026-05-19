massive = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]

def square_lo_shu(massive):
    summa = 15
    ch = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    new_mas = []
    for i in range(len(massive)):
        for j in range(len(massive[i])):
            new_mas.append(massive[i][j])
    for i in range(len(ch)):
        if new_mas.count(ch[i]) != 1:
            print('Не является магическим квадратом Ло Шу.')
            exit()
    if sum(massive[0]) == 15 and sum(massive[1]) == 15 \
        and sum(massive[2]) == 15:
        if (massive[0][0] + massive[1][0] + massive[2][0]) == 15 \
            and (massive[0][1] + massive[1][1] + massive[2][1]) == 15 \
            and (massive[0][2] + massive[1][2] + massive[2][2]) == 15:
            if (massive[0][0] + massive[1][1] + massive[2][2]) == 15 \
                and (massive[2][0] + massive[1][1] + massive[0][2]) == 15:
                print('Является магическим квадратом Ло Шу.')
            else:
                print('Не является магическим квадратом Ло Шу.')
        else:
            print('Не является магическим квадратом Ло Шу.')
    else:
        print('Не является магическим квадратом Ло Шу.')

square_lo_shu(massive)
