# 1

def factorial_rec(n: int) -> int:
    if n == 1:
        return 1
    return n * factorial_rec(n - 1)

def factorial_bez(n: int) -> int:
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x

print(factorial_rec(5))
print(factorial_bez(5))

print("Итеративная функция обычно экономнее по памяти.")
print("Рекурсивная функция короче, но использует стек вызовов.")


# 2

a = [1, 2, 3, 4, 5]

def kvadrat_rec(spisok: list) -> list:
    if not spisok:
        return []
    return [spisok[0] ** 2] + kvadrat_rec(spisok[1:])

def kvadrat_bez(spisok: list) -> list:
    res_spisok = []
    for i in range(len(spisok)):
        res_spisok.append(spisok[i] ** 2)
    return res_spisok

print(kvadrat_bez(a))
print(kvadrat_rec(a))
