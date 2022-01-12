import sqlite3


class DBUser:
    def __init__(self):
        self.__conn = sqlite3.connect('users.db')
        self.__cur = self.__conn.cursor()
        self.create_table()

    def create_table(self):
        self.__cur.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTEGER AUTO_INCREMENT,
            name TEXT,
            weight INTEGER
        )""")

    def close_connect(self):
        self.__conn.close()
    
    
class DBProduct:
    def __init__(self):
        self.__conn = sqlite3.connect('products.db')
        self.__cur = self.__conn.cursor()
        self.__cur.row_factory = sqlite3.Row
        self.create_table()

    def create_table(self):
        self.__cur.execute("""CREATE TABLE IF NOT EXISTS products(
            id INTEGER AUTO_INCREMENT,
            name TEXT,
            proteins INTEGER,
            fat INTEGER,
            carbs INTEGER
        )""")

    def show_all_products(self):
        products = self.__cur.execute("""
            SELECT * FROM products
        """)

        return products.fetchall()

    def close_connect(self):
        self.__conn.close()