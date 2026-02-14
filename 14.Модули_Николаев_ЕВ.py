# 1
from datetime import datetime
import random

current_time = datetime.now()
print(current_time)

# 2
random_list = [random.randint(1, 100) for _ in range(101)]
randomer_number = random.choice(random_list)
print(randomer_number)

# 3
try:
    import matplotlib.pyplot as plt

    number_a = list(range(1, 13))
    number_b = random.sample(range(1000), 12)
    plt.plot(number_a, number_b)
    plt.show()
except Exception as e:
    print("matplotlib недоступен или ошибка построения графика")

# 4
employees = [
    ["Иванов Иван Иванович", "Менеджер", "22.10.2013", 250000],
    ["Сорокина Екатерина Матвеевна", "Аналитик", "12.03.2020", 75000],
    ["Струков Иван Сергеевич", "Старший программист", "23.04.2012", 150000],
    ["Корнеева Анна Игоревна", "Ведущий программист", "22.02.2015", 120000],
    ["Старчиков Сергей Анатольевич", "Младший программист", "12.11.2021", 50000],
    ["Бутенко Артем Андреевич", "Архитектор", "12.02.2010", 200000],
    ["Савченко Алина Сергеевна", "Старший аналитик", "13.04.2016", 100000],
]

def _parse_date(d):
    return datetime.strptime(d, "%d.%m.%Y")

def programmer_day_bonus(employees_list):
    bonuses = []
    for fio, position, hire_date, salary in employees_list:
        if "программист" in position.lower():
            bonuses.append((fio, round(salary * 0.03, 2)))
    return bonuses

def gender_holiday_bonus(employees_list):
    bonuses_8march = []
    bonuses_23feb = []
    for fio, position, hire_date, salary in employees_list:
        parts = fio.split()
        patronymic = parts[2] if len(parts) >= 3 else ""
        is_female = patronymic.endswith("на")
        if is_female:
            bonuses_8march.append((fio, 2000))
        else:
            bonuses_23feb.append((fio, 2000))
    return bonuses_8march, bonuses_23feb

def index_salaries(employees_list):
    updated = []
    now = datetime.now()
    for fio, position, hire_date, salary in employees_list:
        hd = _parse_date(hire_date)
        years = (now - hd).days / 365.25
        rate = 0.07 if years > 10 else 0.05
        new_salary = round(salary * (1 + rate), 2)
        updated.append([fio, position, hire_date, new_salary])
    return updated

def vacation_eligible(employees_list):
    eligible = []
    now = datetime.now()
    for fio, position, hire_date, salary in employees_list:
        hd = _parse_date(hire_date)
        months = (now - hd).days / 30.44
        if months > 6:
            eligible.append(fio)
    return eligible

print(programmer_day_bonus(employees))
print(gender_holiday_bonus(employees))
print(index_salaries(employees))
print(vacation_eligible(employees))

# 5
def digit_sum(n):
    s = 0
    for ch in str(abs(int(n))):
        s += int(ch)
    return s

admin_number = random.randint(1, 9)
print(admin_number)

user_numbers_input = input().strip()
user_numbers = []
if user_numbers_input:
    user_numbers = user_numbers_input.split()

printed = 0
for num in user_numbers:
    if printed >= 5:
        break
    if digit_sum(num) % admin_number == 0:
        print(num)
        printed += 1

# 6
def coin_toss(n):
    for _ in range(n):
        print(random.choice(["Орел", "Решка"]))

def dice_roll(n):
    for _ in range(n):
        print(random.randint(1, 6))

def password_gen(length):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return "".join(random.choice(alphabet) for _ in range(length))

mode = input().strip()

if mode == "1":
    n = int(input().strip())
    coin_toss(n)
elif mode == "2":
    n = int(input().strip())
    dice_roll(n)
elif mode == "3":
    length = int(input().strip())
    print(password_gen(length))
