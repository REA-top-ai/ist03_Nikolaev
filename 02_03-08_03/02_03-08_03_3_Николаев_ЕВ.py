answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
with open('student_solution.txt', 'r') as file:
    massive = list(file)
    for string in massive:
        k = 0
        no_answers = []
        string_n = string.split(', ')
        for i in range(len(string_n)):
            if string_n[i] == answers[i]:
                k += 1
            else:
                no_answers.append(i + 1)

        if k >= 15:
            print('Вы сдали!')
            print(f'{k} правильный ответов')
            print(f'{len(no_answers)} неправильный ответов')
            if no_answers:
                print('Номера неправильный ответов:', no_answers)
        else:
            print('Вы не сдали.')
            print(f'{k} правильный ответов')
            print(f'{len(no_answers)} неправильный ответов')
            print('Номера неправильный ответов:', no_answers)
