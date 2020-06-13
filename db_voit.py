import sqlite3


class DataBaseVot:
    __connection = None

    def get__connection(self):
        if DataBaseVot.__connection is None:
            DataBaseVot.__connection = sqlite3.connect('Voting.db', check_same_thread=False)
        return DataBaseVot.__connection

    def init_db(self, force: bool = False):
        """ Проверить что нужные таблицы существуют, иначе создать их

            Важно: миграции на такие таблицы вы должны производить самостоятельно!

            :param conn: подключение к СУБД
            :param force: явно пересоздать все таблицы
        """
        conn = self.get__connection()
        c = conn.cursor()

        # Информация о пользователе
        # TODO: создать при необходимости...

        # Сообщения от пользователей
        if force:
            c.execute('DROP TABLE IF EXISTS user_message')

        c.execute('''
            CREATE TABLE IF NOT EXISTS voting (
                id          INTEGER PRIMARY KEY,
                user_id     INTEGER NOT NULL,
                candidate      TEXT NOT NULL
            )
        ''')

        # Сохранить изменения
        conn.commit()

    def add_vot(self, user_id: int, candidate):
        conn = self.get__connection()
        c = conn.cursor()
        c.execute('INSERT INTO voting (user_id, status) VALUES (?, ?)', (user_id, candidate))
        conn.commit()

    def vot_exist(self, user_id):
        conn = self.get__connection()
        c = conn.cursor()
        return c.execute('SELECT * FROM voting WHERE (user_id) = ?', (user_id,))

    def get_users(self):
        conn = self.get__connection()
        c = conn.cursor()
        c.execute('SELECT * FROM voting')
        rows = c.fetchall()
        user_ids = []
        for i in rows:
            user_ids.append(i[1])
        return user_ids
