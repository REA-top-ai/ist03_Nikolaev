import os
import time
import requests

from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, render_template, request, session, redirect, url_for
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from werkzeug.utils import secure_filename


load_dotenv()

app = Flask(__name__)

app.secret_key = 'dev-secret-key'

app.config['UPLOAD_FOLDER'] = 'uploads'

# Список расширений файлов, которые можно загружать
ALLOWED_EXTENSIONS = {'mp3', 'wav', 'm4a', 'mp4', 'mov', 'webm', 'avi', 'mkv'}

# Берем строку подключения к PostgreSQL из .env
DATABASE_URL = os.getenv(
    'DATABASE_URL',
    'postgresql+psycopg2://evgeny@localhost:5432/transkribator_rea'
)

# Создаем подключение SQLAlchemy к PostgreSQL
engine = create_engine(DATABASE_URL)

# Base нужен SQLAlchemy для описания таблиц через классы Python
Base = declarative_base()

# SessionLocal создает отдельную сессию для одного действия с базой
# Через сессию мы ищем, добавляем и изменяем записи без ручного SQL
SessionLocal = sessionmaker(bind=engine)


class User(Base):
    # Говорим SQLAlchemy, что этот класс относится к таблице users
    __tablename__ = 'users'

    # Поля таблицы users
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)


class Transcription(Base):
    # Говорим SQLAlchemy, что этот класс относится к таблице transcriptions
    __tablename__ = 'transcriptions'

    # Поля таблицы transcriptions
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    filename = Column(String(255), nullable=False)
    file_path = Column(String(500), nullable=False)
    transcript_text = Column(Text)
    analysis_text = Column(Text)
    created_at = Column(DateTime, default=datetime.now)


def get_db():
    # Создаем новую сессию для работы с PostgreSQL
    db = SessionLocal()

    # Возвращаем сессию в маршрут
    return db

def init_db():
    # SQLAlchemy смотрит на классы User и Transcription
    # и создает их таблицы, если таблиц еще нет
    Base.metadata.create_all(engine)


def allowed_file(filename):
    # Проверяем, есть ли в имени файла точка
    if '.' not in filename:
        return False

    # Берем расширение файла после последней точки
    extension = filename.rsplit('.', 1)[1].lower()

    # Проверяем, есть ли расширение в списке разрешенных
    if extension in ALLOWED_EXTENSIONS:
        return True
    else:
        return False


def make_unique_filename(filename):
    # Делаем безопасное имя файла, чтобы убрать опасные символы
    safe_name = secure_filename(filename)

    # Получаем текущую дату и время
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    # Склеиваем дату и имя файла
    new_filename = f'{timestamp}_{safe_name}'

    # Возвращаем новое имя файла
    return new_filename


def transcribe_file(file_path):
    # Берем ключ AssemblyAI из .env
    api_key = os.getenv('ASSEMBLYAI_API_KEY')

    # Если ключ не найден, сразу возвращаем понятную ошибку
    if not api_key:
        return 'Ошибка: не найден ASSEMBLYAI_API_KEY в файле .env'

    # Проверяем, что файл реально есть на сервере
    if not os.path.exists(file_path):
        return 'Ошибка: файл не найден на сервере'

    # Заголовок authorization нужен AssemblyAI для проверки API-ключа
    headers = {
        'authorization': api_key
    }

    try:
        # Открываем файл в бинарном режиме
        # rb значит read binary, то есть читаем файл как байты
        audio_file = open(file_path, 'rb')

        # Отправляем файл в AssemblyAI
        upload_response = requests.post(
            'https://api.assemblyai.com/v2/upload',
            headers=headers,
            data=audio_file,
            timeout=300
        )

        # Закрываем файл после отправки
        audio_file.close()

        # Если AssemblyAI вернул HTTP-ошибку, Python перейдет в except
        upload_response.raise_for_status()

        # Превращаем ответ AssemblyAI из JSON в обычный Python-словарь
        upload_result = upload_response.json()

        # Достаем ссылку на загруженный файл
        upload_url = upload_result.get('upload_url')

        # Если ссылки нет, значит загрузка прошла неправильно
        if not upload_url:
            return 'Ошибка: AssemblyAI не вернул ссылку на загруженный файл'

        # Данные для создания задачи транскрибации
        transcript_data = {
            'audio_url': upload_url,
            'language_detection': True,
            'speaker_labels': True
        }

        # Создаем задачу транскрибации в AssemblyAI
        transcript_response = requests.post(
            'https://api.assemblyai.com/v2/transcript',
            headers=headers,
            json=transcript_data,
            timeout=60
        )

        # Проверяем, что задача создалась без HTTP-ошибки
        transcript_response.raise_for_status()

        # Превращаем ответ в словарь
        transcript_result = transcript_response.json()

        # Достаем id задачи
        transcript_id = transcript_result.get('id')

        # Если id нет, значит AssemblyAI не создал задачу
        if not transcript_id:
            return 'Ошибка: AssemblyAI не вернул id транскрибации'

        # AssemblyAI делает транскрибацию не сразу
        # Поэтому несколько раз спрашиваем статус задачи
        for attempt in range(120):
            # Ждем 5 секунд между проверками
            time.sleep(5)

            # Запрашиваем текущий статус транскрибации
            status_response = requests.get(
                f'https://api.assemblyai.com/v2/transcript/{transcript_id}',
                headers=headers,
                timeout=60
            )

            # Проверяем HTTP-ошибки
            status_response.raise_for_status()

            # Получаем результат в виде словаря
            result = status_response.json()

            # Достаем статус
            status = result.get('status')

            # Если статус completed, транскрибация готова
            if status == 'completed':
                # utterances - это куски текста с разными спикерами
                utterances = result.get('utterances') or []

                # Если AssemblyAI нашел спикеров, выводим текст по спикерам
                if utterances:
                    lines = []

                    for utterance in utterances:
                        # Получаем букву или номер спикера
                        speaker = utterance.get('speaker', '?')

                        # Получаем текст этого спикера
                        text_line = utterance.get('text', '')

                        # Добавляем строку только если там есть текст
                        if text_line:
                            lines.append(f'Спикер {speaker}: {text_line}')

                    # Склеиваем все строки через перенос строки
                    return '\n'.join(lines)

                # Если спикеров нет, возвращаем простой текст
                simple_text = result.get('text')

                if simple_text:
                    return simple_text
                else:
                    return 'AssemblyAI закончил транскрибацию, но текст пустой.'

            # Если AssemblyAI вернул ошибку в задаче
            if status == 'error':
                error_text = result.get('error', 'неизвестная ошибка')
                return f'Ошибка AssemblyAI: {error_text}'

        # Если цикл закончился, значит мы слишком долго ждали
        return 'Ошибка: AssemblyAI слишком долго обрабатывает файл. Попробуйте позже.'

    except requests.exceptions.RequestException as error:
        # Эта ошибка возникает, если не прошел HTTP-запрос
        return f'Ошибка при запросе к AssemblyAI: {error}'


def analyze_transcript(transcript_text):
    # Берем ключ ProxyAPI из .env
    api_key = os.getenv('OPENAI_API_KEY')

    # Если ключа нет, возвращаем понятную ошибку
    if not api_key:
        return 'Ошибка: не найден OPENAI_API_KEY в файле .env'

    # Берем адрес ProxyAPI из .env
    # Если адреса нет, используем стандартный адрес ProxyAPI
    base_url = os.getenv('OPENAI_BASE_URL', 'https://api.proxyapi.ru/openai/v1')

    # Берем модель из .env
    # gpt-5-nano оставлена как дешевая модель для учебного проекта
    model = os.getenv('OPENAI_MODEL', 'gpt-5-nano')

    # Проверяем, что текст транскрибации не пустой
    if not transcript_text or not transcript_text.strip():
        return 'Сначала нужно сделать транскрибацию.'

    try:
        # Импортируем OpenAI-клиент
        # Он подходит и для ProxyAPI, потому что ProxyAPI работает как OpenAI-compatible API
        from openai import OpenAI

        # Создаем клиента
        # api_key - ключ ProxyAPI
        # base_url - адрес ProxyAPI
        client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )

        # Пишем промпт простым текстом
        prompt = f'''
Проанализируй транскрибацию созвона и найди задачи.

Верни только простой текст на русском языке.
Если задач нет, верни ровно эту фразу:
Явных задач в созвоне не найдено.

Формат, если задачи есть:
Задачи по итогам созвона:

1. Задача: ...
   Ответственный: ...
   Срок: ...

Транскрибация:
{transcript_text}
'''

        # Отправляем запрос в нейросеть
        response = client.responses.create(
            model=model,
            input=[
                {
                    'role': 'system',
                    'content': 'Ты помогаешь находить задачи по тексту созвона.'
                },
                {
                    'role': 'user',
                    'content': prompt
                }
            ],
            max_output_tokens=600
        )

        # Достаем текст ответа
        answer = response.output_text

        # Если ответ есть, возвращаем его
        if answer and answer.strip():
            return answer.strip()

        # Если ответ почему-то пустой, возвращаем простой текст
        return 'Явных задач в созвоне не найдено.'

    except ImportError:
        # Эта ошибка будет, если пакет openai не установлен
        return 'Ошибка: пакет openai не установлен. Установите зависимости из requirements.txt'

    except Exception as error:
        # Любую другую ошибку показываем простым текстом
        return f'Ошибка при анализе через ProxyAPI: {error}'


@app.route('/', methods=['GET'])
def index():
    # Показываем страницу входа
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    # Получаем имя пользователя из формы
    username = request.form.get('username', '').strip()

    # Получаем пароль из формы
    password = request.form.get('pw')

    # Проверяем, что пользователь ввел логин и пароль
    if not username or not password:
        return render_template('index.html', error='Введите логин и пароль')

    # Открываем сессию для работы с базой
    db = get_db()

    # Ищем пользователя по имени
    # SQLAlchemy сам составит SELECT-запрос к таблице users
    user = db.query(User).filter_by(username=username).first()

    # Закрываем сессию после поиска
    db.close()

    # Если пользователь не найден, показываем ошибку
    if user is None:
        return render_template('index.html', error='Неверный логин или пароль')

    # В учебной версии пароль хранится простым текстом
    # password_hash осталось названием поля, потому что такое поле уже было в проекте
    if user.password_hash != password:
        return render_template('index.html', error='Неверный логин или пароль')

    # Запоминаем id пользователя в session
    session['user_id'] = user.id

    # Запоминаем имя пользователя в session
    session['username'] = user.username

    # После входа отправляем пользователя в личный кабинет
    return redirect(url_for('dashboard'))


@app.route('/dashboard')
def dashboard():
    # Проверяем, вошел ли пользователь
    if 'user_id' not in session:
        return redirect(url_for('index'))

    # Показываем личный кабинет
    return render_template(
        'dashboard.html',
        username=session['username'],
        user_id=session['user_id']
    )


@app.route('/upload', methods=['POST'])
def upload_file():
    # Проверяем, вошел ли пользователь
    if 'user_id' not in session:
        return redirect(url_for('index'))

    # Проверяем, что файл есть в форме
    if 'meeting_file' not in request.files:
        return 'Файл не найден в форме'

    # Достаем файл из формы
    file = request.files['meeting_file']

    # Проверяем, что пользователь выбрал файл
    if file.filename == '':
        return 'Файл не выбран'

    # Проверяем расширение файла
    if not allowed_file(file.filename):
        return 'Недопустимый формат файла'

    # Создаем безопасное уникальное имя файла
    filename = make_unique_filename(file.filename)

    # Собираем путь к папке пользователя
    user_folder = os.path.join(
        app.config['UPLOAD_FOLDER'],
        str(session['user_id'])
    )

    # Создаем папку пользователя, если ее еще нет
    os.makedirs(user_folder, exist_ok=True)

    # Собираем полный путь к файлу
    file_path = os.path.join(user_folder, filename)

    # Сохраняем файл на сервер
    file.save(file_path)

    # Открываем сессию для работы с базой
    db = get_db()

    # Создаем новую запись таблицы transcriptions
    new_transcription = Transcription(
        user_id=session['user_id'],
        filename=filename,
        file_path=file_path
    )

    # Добавляем новую запись в сессию
    db.add(new_transcription)

    # Сохраняем новую запись в PostgreSQL
    db.commit()

    # Закрываем сессию
    db.close()

    # После загрузки отправляем пользователя в историю
    return redirect(url_for('history'))


@app.route('/history')
def history():
    # Проверяем, вошел ли пользователь
    if 'user_id' not in session:
        return redirect(url_for('index'))

    # Открываем сессию для работы с базой
    db = get_db()

    # Берем только записи текущего пользователя
    # order_by нужен, чтобы новые записи показывались сверху
    transcriptions = db.query(Transcription).filter_by(
        user_id=session['user_id']
    ).order_by(Transcription.id.desc()).all()

    # Закрываем сессию после чтения списка
    db.close()

    # Показываем страницу истории
    return render_template('history.html', transcriptions=transcriptions)


@app.route('/transcribe/<int:transcription_id>', methods=['POST'])
def transcribe(transcription_id):
    # Проверяем, вошел ли пользователь
    if 'user_id' not in session:
        return redirect(url_for('index'))

    # Открываем сессию для работы с базой
    db = get_db()

    # Ищем запись только текущего пользователя
    # Два условия защищают от доступа к чужим записям:
    # id - номер нужной записи, user_id - владелец записи
    transcription = db.query(Transcription).filter_by(
        id=transcription_id,
        user_id=session['user_id']
    ).first()

    # Если запись не найдена, закрываем базу и показываем ошибку
    if transcription is None:
        db.close()
        return 'Запись не найдена'

    # Отправляем файл в AssemblyAI и получаем текст
    transcript_text = transcribe_file(transcription.file_path)

    # Сохраняем текст транскрибации в базу
    # Мы меняем поле объекта, а SQLAlchemy сам сделает UPDATE
    transcription.transcript_text = transcript_text

    # Сохраняем изменения
    db.commit()

    # Закрываем сессию
    db.close()

    # Возвращаем пользователя в историю
    return redirect(url_for('history'))


@app.route('/analyze/<int:transcription_id>', methods=['POST'])
def analyze(transcription_id):
    # Проверяем, вошел ли пользователь
    if 'user_id' not in session:
        return redirect(url_for('index'))

    # Открываем сессию для работы с базой
    db = get_db()

    # Ищем запись только текущего пользователя
    # Так пользователь не сможет анализировать чужую транскрибацию
    transcription = db.query(Transcription).filter_by(
        id=transcription_id,
        user_id=session['user_id']
    ).first()

    # Если запись не найдена, закрываем базу и показываем ошибку
    if transcription is None:
        db.close()
        return 'Запись не найдена'

    # Проверяем, что транскрибация уже сделана
    if not transcription.transcript_text:
        db.close()
        return 'Сначала нужно сделать транскрибацию.'

    # Отправляем текст транскрибации в нейросеть
    analysis_text = analyze_transcript(transcription.transcript_text)

    # Сохраняем анализ в базу
    # Мы меняем поле объекта, а SQLAlchemy сам выполнит UPDATE
    transcription.analysis_text = analysis_text

    # Сохраняем изменения
    db.commit()

    # Закрываем сессию
    db.close()

    # Возвращаем пользователя в историю
    return redirect(url_for('history'))


@app.route('/logout')
def logout():
    # Очищаем session
    session.clear()

    # Возвращаем пользователя на страницу входа
    return redirect(url_for('index'))


@app.route('/register')
def register():
    # Показываем страницу регистрации
    return render_template('register.html')


@app.route('/newreg', methods=['POST'])
def newreg():
    # Получаем имя пользователя из формы
    username = request.form.get('username', '').strip()

    # Получаем пароль из формы
    password = request.form.get('pw')

    # Получаем повтор пароля из формы
    password_check = request.form.get('pw_check')

    # Проверяем, что все поля заполнены
    if not username or not password or not password_check:
        return render_template('register.html', error='Заполните все поля')

    # Проверяем, что пароли совпадают
    if password != password_check:
        return render_template('register.html', error='Пароли не совпадают')

    # Открываем сессию для работы с базой
    db = get_db()

    # Проверяем, есть ли уже пользователь с таким именем
    existing_user = db.query(User).filter_by(username=username).first()

    # Если пользователь уже есть, закрываем базу и показываем ошибку
    if existing_user is not None:
        db.close()
        return render_template('register.html', error='Такой юзер уже есть')

    # В учебной версии сохраняем пароль простым текстом
    # Поле называется password_hash только потому, что такое имя уже было в проекте
    password_hash = password

    # Создаем объект нового пользователя
    new_user = User(
        username=username,
        password_hash=password_hash
    )

    # Добавляем нового пользователя в сессию
    db.add(new_user)

    # Сохраняем изменения
    db.commit()

    # Закрываем сессию
    db.close()

    # Показываем простой текст после регистрации
    return f'Пользователь {username} зарегистрирован'


# При запуске приложения создаем таблицы, если их нет
init_db()


if __name__ == '__main__':
    # Запускаем Flask в режиме разработки
    app.run(debug=True)
