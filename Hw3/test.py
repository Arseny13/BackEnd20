import logging
import psycopg2
from prettytable import PrettyTable

logger = logging.getLogger("App.Class ")

def from_request(attr):
    """получение параметров"""
    if attr.isdigit():
        return "INT NOT NULL,"
    return "VARCHAR(50)"

class orm:
    def __init__(self, table_name='MyTable'):
        """инициализация"""
        self.table_name = table_name
        self.connect = None
        self.cursor = None
        self.connection()

    def connection(self):
        """метод подкоючение к бд"""
        if self.connect is None:
            self.connect = psycopg2.connect(database="postgres",
                                            user="postgres",
                                            password="1234",
                                            host="localhost",
                                            port="5432")
        if self.cursor is None:
            self.cursor = self.connect.cursor()

    def print(self, counter=0):
        """метод печати """
        count = 0
        description_list = [self.cursor.description[index][0]
                            for index, _ in enumerate(self.cursor.description)]
        table = PrettyTable(description_list)
        for row in self.cursor:
            table.add_row(row)
            count += 1
        print(table)
        if counter == 1:
            print(f'Количество {count} ')
        print()

    def get_all(self):
        """
        Получение и вывод всей таблицы
        """
        self.cursor.execute(f'SELECT * FROM {self.table_name} ORDER BY id;')
        self.print()

    def drop(self):
        """удаление таблицы"""
        self.cursor.execute(f'DROP TABLE {self.table_name};')
        self.connect.commit()
        self.close()
        logger.info("table drop ")

    def close(self):
        """метод отключение от бд"""
        if not self.cursor.closed:
            self.cursor.close()
        if not self.connect.closed:
            self.connect.close()

class Person (orm):
    """класс записи"""
    def __init__(self,name):
        """создание"""

        self.attr = ['name','age','email','phone']
        self.table = orm(table_name = name)
        res = f'CREATE TABLE IF NOT EXISTS {self.table.table_name} ( id BIGSERIAL NOT NULL PRIMARY KEY,'
        for i in self.attr:
            attr = from_request(i)
            res += f'{i} {attr} ,'
        res = res[0:-1]
        res += ');'
        self.table.cursor.execute(res)
        print(f'table %s create', self.table.table_name)
        self.table.connect.commit()



    def create(self,**data):
        res1 = ''
        res2 = ''
        for key, value in data.items():
            res1 += f"{key}, "
            res2 += f"'{value}', "
        res1 = res1[0:-2]
        res2 = res2[0:-2]
        res = f'INSERT INTO {self.table.table_name} ( {res1}) VALUES ( {res2})'
        logger.debug('request add without id = %s', res)
        self.table.cursor.execute(res)
        self.table.connect.commit()

    def get(self,**data):
        """
        Получение строк
        """
        try:
            res = ''
            get_name = ''
            for key, value in data.items():
                get_name+=f'{value}'
            get = Person(f'get{get_name}')

            for key, value in data.items():
                res += f"{key} = '{value}' AND  "
            res = res[0:-5]
            self.table.cursor.execute(f"SELECT * FROM {self.table.table_name} WHERE  {res} ")
            for record in self.table.cursor:
                res = {}
                for i in range(1,len(record)):
                    res[ self.attr[i-1] ] = record[i]
                get.create(**res)
            logger.info("get succesful ")
        except psycopg2.errors.InvalidTextRepresentation:
            logger.error("get Error InvalidText")
        self.table.connect.commit()
        return get

    def save(self, **data):
        res = ''
        for key, value in data.items():
            res += f"{key} = '{value}' AND  "
        res = res[0:-5]
        #print(res)
        self.table.cursor.execute(f'SELECT * FROM {self.table.table_name} ORDER BY id;')
        #print(self.table.table_name)
        output = self.table.cursor.fetchone()
        while output is not None:
            #print('out ', output)
            res1 = ''
            for i in range(1, len(output)):
                res1 += f"{self.attr[i - 1]} = '{output[i]}' AND "
            print(res1)
            res1 = res1[0:-4]
            output = self.table.cursor.fetchone()
        self.table.cursor.execute(f"UPDATE {self.table.table_name} SET {res} WHERE {res1}")

    def delete(self, **data):
        """
        Удаление строк
        """
        try:
            res = ''
            for key, value in data.items():
                res += f"{key} = '{value}' AND  "
            res = res[0:-5]
            logger.debug('request delete  = %s', res)
            self.table.cursor.execute(f"DELETE FROM {self.table.table_name} WHERE {res}")
            logger.info("delete succesful ")
        except psycopg2.errors.InvalidTextRepresentation:
            logger.error("delete Error: InvalidText ")
        self.table.connect.commit()

    def all(self):
        self.table.get_all()

    def drop(self):
        self.table.drop()



