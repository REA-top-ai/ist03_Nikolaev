import random


# Задача 1
def task1_magic8():
    name = "Евгений"
    question = "Стоит ли мне сегодня учить Python?"
    answer = ""

    random_number = random.randint(1, 9)

    if random_number == 1:
        answer = "Да, безусловно."
    elif random_number == 2:
        answer = "Это решительно так."
    elif random_number == 3:
        answer = "Без сомнения."
    elif random_number == 4:
        answer = "Ответ туманный, попробуйте еще раз."
    elif random_number == 5:
        answer = "Спросите еще раз позже."
    elif random_number == 6:
        answer = "Лучше не говорить вам сейчас."
    elif random_number == 7:
        answer = "Мои источники говорят «нет»."
    elif random_number == 8:
        answer = "Прогноз не очень хороший."
    elif random_number == 9:
        answer = "Очень сомнительно."
    else:
        answer = "Ошибка"

    if question.strip() == "":
        print("Вы не задали вопрос. Магический шар не может отвечать на пустоту :)")
        return

    if name.strip() == "":
        print(f"Вопрос: {question}")
    else:
        print(f"{name} спрашивает: {question}")

    print(f"Магический шар отвечает: {answer}")


# Задача 2
def task2_outliers():
    max_value = float(input("Введите максимум: "))
    mean_value = float(input("Введите среднее: "))
    min_value = float(input("Введите минимум: "))
    std_value = float(input("Введите стандартное отклонение: "))

    if std_value < 0:
        print("Стандартное отклонение не может быть отрицательным.")
        return

    if (max_value > mean_value + 5 * std_value) or (min_value < mean_value - 5 * std_value):
        print("В ваших данных имеются экстремальные значения и требуют предобработки")
    elif (max_value > mean_value + 3 * std_value) or (min_value < mean_value - 3 * std_value):
        print("В ваших данных имеются выбросы и требуют предобработки")
    else:
        print("Ваши данные пригодны для анализа")


# Задача 3
def task3_age_check():
    age_of_user = int(input("Введите возраст пользователя: "))
    age_limit = int(input("Введите возрастное ограничение: "))

    if age_of_user >= age_limit:
        print("Приятного просмотра!")
    else:
        print("Извините, ваш возраст не соответствует введенным возрастным ограничениям")


# Задача 4
def task4_carsharing_price():
    brand = input("Введите марку (Volkswagen Polo / BMW X1): ").strip()
    age = int(input("Введите возраст водителя: "))
    experience = int(input("Введите стаж (лет): "))
    reputation = int(input("Введите репутацию (1-5): "))
    traffic = int(input("Введите пробки (1-7): "))
    minutes = int(input("Введите длительность поездки (в минутах): "))

    def in_range(x, a, b):
        return a <= x <= b

    age_20_27 = in_range(age, 20, 27)
    age_27_34 = in_range(age, 27, 34)

    exp_2_9 = in_range(experience, 2, 9)
    exp_10_15 = in_range(experience, 10, 15)

    rep_1_2 = in_range(reputation, 1, 2)
    rep_3_5 = in_range(reputation, 3, 5)

    traffic_1_3 = in_range(traffic, 1, 3)
    traffic_4_7 = in_range(traffic, 4, 7)

    tariff = None

    if brand.lower() in ["volkswagen polo", "volkswagen", "polo", "volkswagen_polo"]:
        if age_20_27 and exp_2_9 and rep_1_2 and traffic_1_3:
            tariff = 8.0
        elif age_20_27 and exp_2_9 and rep_1_2 and traffic_4_7:
            tariff = 8.5
        elif age_20_27 and exp_2_9 and rep_3_5 and traffic_1_3:
            tariff = 7.5
        elif age_20_27 and exp_2_9 and rep_3_5 and traffic_4_7:
            tariff = 7.4
        elif age_27_34 and exp_2_9 and rep_1_2 and traffic_1_3:
            tariff = 7.2
        elif age_27_34 and exp_2_9 and rep_3_5 and traffic_1_3:
            tariff = 7.0
        elif age_27_34 and exp_2_9 and rep_3_5 and traffic_4_7:
            tariff = 7.2
        elif age_27_34 and exp_10_15 and rep_1_2 and traffic_1_3:
            tariff = 6.9
        elif age_27_34 and exp_10_15 and rep_3_5 and traffic_4_7:
            tariff = 6.6
        elif age_27_34 and exp_10_15 and rep_1_2 and traffic_4_7:
            tariff = 6.7

    elif brand.lower() in ["bmw x1", "bmw", "x1", "bmw_x1"]:
        if age_20_27 and exp_2_9 and rep_1_2 and traffic_1_3:
            tariff = 12.0
        elif age_20_27 and exp_2_9 and rep_1_2 and traffic_4_7:
            tariff = 12.5
        elif age_20_27 and exp_2_9 and rep_3_5 and traffic_1_3:
            tariff = 11.6
        elif age_20_27 and exp_2_9 and rep_3_5 and traffic_4_7:
            tariff = 11.3
        elif age_27_34 and exp_2_9 and rep_1_2 and traffic_1_3:
            tariff = 11.4
        elif age_27_34 and exp_2_9 and rep_3_5 and traffic_1_3:
            tariff = 11.7
        elif age_27_34 and exp_2_9 and rep_3_5 and traffic_4_7:
            tariff = 11.9
        elif age_27_34 and exp_10_15 and rep_1_2 and traffic_1_3:
            tariff = 10.8
        elif age_27_34 and exp_10_15 and rep_3_5 and traffic_4_7:
            tariff = 10.9
        elif age_27_34 and exp_10_15 and rep_1_2 and traffic_4_7:
            tariff = 11.0

    if tariff is None:
        print("Тариф по введенным условиям не найден (проверь диапазоны/марку).")
        return

    price = minutes * tariff
    print(f"Стоимость вашей поездки составит {price}")



# Задача 5
def task5_coffee_recipe():
    coffee = input("Введите название кофе (Капучино/Латте/Фрапучино/Эспрессо): ").strip().lower()

    cappuccino = (
        "Капучино\n"
        "1. Сварите кофе (турка: доведите до кипения 2-3 раза / френч-пресс). Процедите, налейте в подогретую кружку.\n"
        "2. Подогрейте молоко (не перегревайте выше ~65°C).\n"
        "3. Взбейте блендером/миксером до однородной пены без крупных пузырьков.\n"
        "4. Влейте взбитую массу в кофе.\n"
    )

    latte = (
        "Латте\n"
        "1. Заварите кофе любым удобным способом (кофе должен быть достаточно крепким).\n"
        "2. Разогрейте молоко до 50-60°C (не кипятить).\n"
        "3. Взбейте молоко 4-5 минут до воздушной пены.\n"
        "4. Перелейте молоко в высокий бокал.\n"
        "5. Аккуратно тонкой струйкой влейте кофе, чтобы получились слои: молоко, кофе, пена.\n"
        "6. По желанию добавьте корицу/шоколад.\n"
    )

    frappuccino = (
        "Фрапучино\n"
        "1. Сварите и охладите кофе (можно заменить зелёным чаем, ~150 мл).\n"
        "2. Поместите компоненты в блендер и взбивайте до мелкой крошки льда.\n"
        "3. Взбейте охлажденные сливки миксером до устойчивой формы.\n"
        "4. Перелейте кофе в бокал и украсьте сливками. Подавайте холодным.\n"
    )

    espresso = (
        "Эспрессо\n"
        "1. В чашку с толстыми стенками насыпьте растворимый кофе и сахар (на одну порцию).\n"
        "2. Добавьте немного кипятка и интенсивно взбивайте ложкой.\n"
        "3. Масса посветлеет и станет похожа на сметану.\n"
        "4. Аккуратно долейте оставшуюся воду, помешивая до образования густой пены.\n"
    )

    if coffee == "капучино":
        print(cappuccino)
    elif coffee == "латте":
        print(latte)
    elif coffee == "фрапучино":
        print(frappuccino)
    elif coffee == "эспрессо":
        print(espresso)
    else:
        print("Такого напитка нет в списке. Доступно: Капучино, Латте, Фрапучино, Эспрессо.")


# Задача 6

def task6_speech_generator():
    col1 = [
        "Коллеги,",
        "Друзья,",
        "Уважаемые коллеги,",
        "Команда,",
        "Партнёры,",
        "Господа,",
        "Коллеги и друзья,",
        "Уважаемые участники,",
    ]
    col2 = [
        "прагматичный подход к цифровым платформам",
        "стратегическое мышление в рамках продукта",
        "фокус на ценности для клиента",
        "операционная дисциплина в процессах",
        "системная работа с метриками",
        "ориентация на устойчивый рост",
        "управление изменениями в команде",
        "переосмысление бизнес-модели",
    ]
    col3 = [
        "несёт в себе риски",
        "даёт возможность",
        "позволяет выявить",
        "открывает потенциал",
        "формирует условия",
        "создаёт предпосылки",
        "приводит к эффекту",
        "ускоряет достижение",
    ]
    col4 = [
        "синергетического эффекта",
        "масштабирования гипотез",
        "оптимизации ресурсов",
        "повышения прозрачности",
        "роста качества решений",
        "снижения издержек",
        "улучшения коммуникаций",
        "повышения предсказуемости",
    ]
    col5 = [
        "непроверенных гипотез.",
        "в условиях неопределенности.",
        "при ограниченных ресурсах.",
        "в краткосрочной перспективе.",
        "на горизонте квартала.",
        "в рамках текущей стратегии.",
        "в целях устойчивого роста.",
        "с учетом обратной связи.",
    ]

    a = random.randint(1, 8) - 1
    b = random.randint(1, 8) - 1
    c = random.randint(1, 8) - 1
    d = random.randint(1, 8) - 1
    e = random.randint(1, 8) - 1

    phrase = f"{col1[a]} {col2[b]} {col3[c]} {col4[d]} {col5[e]}"
    print(phrase)


def main():
    print("Самостоятельная работа 3.1 — выберите задачу:")
    print("1 — Magic 8-Ball")
    print("2 — Выбросы/экстремальные значения")
    print("3 — Возрастной доступ")
    print("4 — Тариф каршеринга")
    print("5 — Рецепт кофе")
    print("6 — Генератор речей")
    choice = input("Введите номер (1-6): ").strip()

    if choice == "1":
        task1_magic8()
    elif choice == "2":
        task2_outliers()
    elif choice == "3":
        task3_age_check()
    elif choice == "4":
        task4_carsharing_price()
    elif choice == "5":
        task5_coffee_recipe()
    elif choice == "6":
        task6_speech_generator()
    else:
        print("Неверный выбор.")


if __name__ == "__main__":
    main()
