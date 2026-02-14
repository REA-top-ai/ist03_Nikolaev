# 1
def create_spreadsheet(title):
    print("Создание электронной таблицы с именем " + title)

# 2
create_spreadsheet("Загрузки")

print()

# 3 + 4
def create_spreadsheet(title, row_count=1000):
    print("Создание электронной таблицы с названием " + title + " with " + str(row_count) + " lines")

# 5
create_spreadsheet("Приложения", 10)
