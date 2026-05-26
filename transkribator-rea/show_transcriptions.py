from app import get_db, User, Transcription


# Открываем сессию SQLAlchemy
db = get_db()

# Получаем все записи транскрибаций
# Сначала показываем самые новые записи
transcriptions = db.query(Transcription).order_by(Transcription.id.desc()).all()

# Если записей нет, выводим простой текст
if not transcriptions:
    print('Записей транскрибаций пока нет')
else:
    # Показываем каждую запись
    for item in transcriptions:
        # По user_id находим пользователя, которому принадлежит запись
        user = db.query(User).filter_by(id=item.user_id).first()

        # Если пользователь найден, берем его имя
        if user:
            username = user.username
        else:
            username = 'Пользователь не найден'

        print('ID записи:', item.id)
        print('ID пользователя:', item.user_id)
        print('Username:', username)
        print('Файл:', item.filename)
        print('Путь:', item.file_path)
        print('Транскрибация:', item.transcript_text)
        print('Анализ:', item.analysis_text)
        print('Дата:', item.created_at)
        print('-' * 50)

# Закрываем сессию после чтения данных
db.close()
