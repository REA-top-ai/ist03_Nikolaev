# 1
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp

f100_in_celsius = f_to_c(100)

def c_to_f(c_temp):
    f_temp = c_temp * (9 / 5) + 32
    return f_temp

c0_in_fahrenheit = c_to_f(0)

print(f100_in_celsius)
print(c0_in_fahrenheit)

print()

# 2
def get_force(mass, acceleration):
    return mass * acceleration

train_mass = 22680
train_acceleration = 10
train_force = get_force(train_mass, train_acceleration)

print(train_force)
print("Поезд GE поставляет", train_force, "ньютонов силы")

def get_energy(mass, c=3 * 10 ** 8):
    return mass * (c ** 2)

bomb_mass = 1
bomb_energy = get_energy(bomb_mass)

print("1 кг бомбы составляет", bomb_energy, "Джоулей")

def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance

train_distance = 100
train_work = get_work(train_mass, train_acceleration, train_distance)

print("Поезд выполняет", train_work, "Джоулей за", train_distance, "метров.")

print()

# 3
def wardrobe_message(clothes, time_of_day):
    print("У меня большой гардероб")
    print("Утром лучше всего подходит", clothes)
    print("Днем лучше всего подходит", clothes)
    print("Вечером лучше всего подходит", clothes)
    print("Ночью лучше всего подходит", clothes)

clothes = "домашняя одежда"
wardrobe_message(clothes, "")

print()

def meal_message(meal):
    print("мои предпочтения в еде")
    print("На завтрак лучше всего подходит", meal)
    print("На обед лучше всего подходит", meal)
    print("На ужин лучше всего подходит", meal)

meal = "каша"
meal_message(meal)

print()

# 4
def access_message(user_name):
    dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
    welcome_message = "Добро пожаловать"
    if user_name == "Дмитрий":
        return dmitriy_check
    return welcome_message

print(access_message("Дмитрий"))
print(access_message("Ангелина"))

print()

def access_message_with_arm(user_name, arm):
    dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
    if (user_name == "Дмитрий" and arm == 1) or (user_name == "Ангелина" and arm == 2) or (user_name == "Василий" and arm == 3) or (user_name == "Екатерина" and arm == 4):
        return "Добро пожаловать!"
    if user_name == "Дмитрий":
        return dmitriy_check
    return "Логин или пароль не верный, попробуйте еще раз"

print(access_message_with_arm("Дмитрий", 2))
print(access_message_with_arm("Ангелина", 2))

print()

# 5
def grade_letter(grade):
    if grade >= 4.0:
        return "A"
    elif grade >= 3.0:
        return "B"
    elif grade >= 2.0:
        return "C"
    elif grade >= 1.0:
        return "D"
    else:
        return "F"

grade = 3.6
print(grade_letter(grade))
