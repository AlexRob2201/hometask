from main import MySql
import unittest
import time

class MyShop(MySql):
    def create_shop(self):
        try:
            _query = "CREATE TABLE IF NOT EXISTS shop (id INT AUTO_INCREMENT PRIMARY KEY, item VARCHAR(255), price INT)"
            self.execute_query(_query)
            print('Таблиця успішно створена')
        except Exception:
            print(f'Помилка при створенні таблиці {Exception}')
        
    def add_item(self, item, price):
        try:
            _query = "INSERT INTO shop (item, price) VALUES (%s, %s)"
            _values = (item, price)
            self.execute_query(_query, _values)
            print('Товар додано')
        except Exception:
            print(f'Помилка при додаванні товару {Exception}')
    
    def delete_item(self, item):
        try:
            _query = "DELETE FROM shop WHERE item = %s"
            _values = (item,)
            self.execute_query(_query, _values)
            print('Товар видалено успішно')
        except Exception:
            print(f'При видаленні сталася помилка {Exception}')
            
    def delete_shop(self):
        try:
            _query = "DROP TABLE IF EXISTS shop"
            self.execute_query(_query)
            print('Таблицю видалено успішно')
        except Exception:
            print(f'При видаленні сталася помилка {Exception}')
    
    
if __name__ == "__main__":
    host = 'mysql_application'
    user = 'root'
    password = 'password'
    database = 'app'

    while True:
        try:
            time.sleep(10)
            db = MySql(host, user, password, database)
            if db:
                print('Succesfully connected')            
        except Exception as e:
            print(f'Wait for SQL: {e}')

    MyShop.create_shop()
    
    MyShop.add_item("item_1", 100)
    MyShop.add_item("item_2", 200)
    
    MyShop.delete_item("item_1")
    
    MyShop.delete_shop()
