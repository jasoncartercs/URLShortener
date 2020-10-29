import sqlite3
from sqlite3 import Error
from url_shortner_model import UrlShortenerModel


class DBConnect:
    def __init__(self, db_file):
        self.db_file = db_file

    def __create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except Error as e:
            print(e)

        return conn

    def is_long_url_in_database(self, long_url):
        is_long_url_in_database = False
        conn = self.__create_connection()
        if conn:
            with conn:
                cursor = conn.cursor()
                cursor.execute("SELECT count(*) FROM url where long_url =?", (long_url,))

                result = cursor.fetchone()
                if result[0] == 1:
                    is_long_url_in_database = True

        return is_long_url_in_database

    def is_short_url_in_database(self, short_url):
        is_short_url_in_database = False
        conn = self.__create_connection()
        if conn:
            with conn:
                cursor = conn.cursor()
                cursor.execute("SELECT count(*) FROM url where short_url =?", (short_url,))

                result = cursor.fetchone()
                if result[0] == 1:
                    is_short_url_in_database = True

        return is_short_url_in_database

    def get_shortened_url(self, long_url):
        url_shortener_model = UrlShortenerModel(0, long_url, "")

        conn = self.__create_connection()
        if conn:
            with conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM url where long_url=?", (long_url,))
                result = cursor.fetchone()
                url_shortener_model = UrlShortenerModel(result[0], result[1], result[2])

        return url_shortener_model


    def insert_url(self, url_shortner_model):
        conn = self.__create_connection()
        with conn:
            sql = 'INSERT INTO url(long_url ,short_url ) VALUES(?,?)'
            cursor = conn.cursor()
            cursor.execute(sql, (url_shortner_model.long_url, url_shortner_model.short_url))
            conn.commit()




