from app import get_db, User


# Открываем сессию SQLAlchemy
db = get_db()

# Получаем всех пользователей из таблицы users
users = db.query(User).all()

# Если пользователей нет, выводим простой текст
if not users:
    print('Пользователей пока нет')
else:
    # Показываем данные каждого пользователя
    for user in users:
        print('ID:', user.id)
        print('Username:', user.username)
        print('Password:', user.password_hash)
        print('-' * 40)

# Закрываем сессию после чтения данных
db.close()
