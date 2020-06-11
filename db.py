import sqlite3

__connection = None


def get__connection():
    global __connection
    if __connection is None:
        __connection = sqlite3.connect('Users.db', check_same_thread=False)
    return __connection


def init_db(force: bool = False):
    """ Проверить что нужные таблицы существуют, иначе создать их

        Важно: миграции на такие таблицы вы должны производить самостоятельно!

        :param conn: подключение к СУБД
        :param force: явно пересоздать все таблицы
    """
    conn = get__connection()
    c = conn.cursor()

    # Информация о пользователе
    # TODO: создать при необходимости...

    # Сообщения от пользователей
    if force:
        c.execute('DROP TABLE IF EXISTS user_message')

    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id          INTEGER PRIMARY KEY,
            user_id     INTEGER NOT NULL,
            status      TEXT NOT NULL
        )
    ''')

    # Сохранить изменения
    conn.commit()


def add_user(user_id: int, status):
    conn = get__connection()
    c = conn.cursor()
    c.execute('INSERT INTO users (user_id, status) VALUES (?, ?)', (user_id, status))
    conn.commit()


def subscriber_exist(user_id):
    conn = get__connection()
    c = conn.cursor()
    return c.execute('SELECT * FROM users WHERE (user_id) = ?', (user_id,))


