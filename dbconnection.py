import sqlite3
from setup_logger import logger
"""singleton class to deal with db"""


class DBConnection:

    def __init__(self):
        self.name = 'database.db'
        # connect take url, dbname, user-id, password
        try:
            self.conn = sqlite3.connect(self.name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            logger.error(e)

    def close_db(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def create_db(self):
        SQL_DELETE = """DROP TABLE IF EXISTS articles;"""
        SQL_STATEMENT = """CREATE TABLE articles (id INTEGER PRIMARY KEY AUTOINCREMENT, image text, title text NOT NULL, categorie text);"""
        self.cursor.execute(SQL_DELETE)
        self.cursor.execute(SQL_STATEMENT)

    def insert_db(self, query_plus):
        # query = """INSERT or REPLACE INTO articles (image, title, categorie ) VALUES """
        query = f"use database;INSERT or REPLACE INTO articles (image, title, categorie ) VALUES {query_plus}"
        print(query)
        exit()
        self.cursor.execute(query)

    def select_from_db(self):
        query = 'use database;SELECT * FROM articles;'
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for i in result:
            print(i)
