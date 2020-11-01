"""Class ORM"""
import logging
import psycopg2
from prettytable import PrettyTable


def from_request(attr):
    """получение параметров"""
    if attr.isdigit():
        return "INT NOT NULL,"
    return "VARCHAR(50)"


class Person:
    """класс записи"""
    def __init__(self, id: int = None, name: str = None , age: int= None, email: str = None):
        """создание"""
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.attr = ['id','name','age','email']

    def active_attr(self):
        """метод получение активных атрибутов"""
        result = []
        for i in self.attr:
            attr = getattr(self, i)
            if attr is not None:
                result.append(i)
        return result

    def request(self, char :str):
        """создание запроса через запятую"""
        active = self.active_attr()
        res = ''
        for i in active:
            attr = getattr(self, i)
            res += f"{i} = '{attr}' {char} "
        if char is ",":
            res = res[0:-2]
        elif char is 'AND':
            res = res[0:-5]
            res += ';'
        return res


logger = logging.getLogger("App.Class ")

class MyOrm(Person):
    """класс орм """

    def __init__(self, table_name = 'MyTable'):
        """инициализация"""
        self.table_name = table_name
        self.connect = None
        self.cursor = None
        self.connection()
        persona = Person()
        attribute = persona.attr
        attribute.pop(0)
        res = f'CREATE TABLE IF NOT EXISTS {self.table_name} ( id BIGSERIAL NOT NULL PRIMARY KEY,'
        for i in attribute:
            attr = from_request(i)
            res += f'{i} {attr} ,'
        res = res[0:-1]
        res += ');'
        self.cursor.execute(res)
        logger.info('table %s create', self.table_name)
        self.connect.commit()

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

    def create(self, per:Person):
        """создание строки"""
        try:
            attr = per.attr
            active_attr = per.active_attr()
            if active_attr[0] != attr[0]:
                attr.pop(0)
                res = f'INSERT INTO {self.table_name} ('
                res += ', '.join(attr)
                res += ') '
                res += 'VALUES ('
                for i in attr:
                    get = getattr(per, i)
                    if isinstance(get, int) and get is not None:
                        res += f' {get},'
                    else:
                        res += f" '{get}' ,"
                res = res[0:-1]
                res += ')'
                logger.debug('request add without id = %s',res)
                self.cursor.execute(res)
                self.connect.commit()
            else:
                res = f'INSERT INTO {self.table_name} ('
                res += ', '.join(attr)
                res += ') '
                res += 'VALUES ('
                for i in attr:
                    get = getattr(per, i)
                    if isinstance(get, int) and get is not None:
                        res += f' {get},'
                    else:
                        res += f" '{get}' ,"
                res = res[0:-1]
                res += ')'
                logger.debug('request add with id = %s', res)
                self.cursor.execute(res)
                logger.info('add Person')
        except psycopg2.errors.UniqueViolation:
            logger.error('error create: already ID')
        except psycopg2.errors.InvalidTextRepresentation:
            logger.error('error create: InvalidText')
        self.connect.commit()

    def get(self,per:Person):
        """
        Получение строк
        """
        try:
            res = per.request('AND')
            logger.debug('request get  = %s', res)
            self.cursor.execute(f"SELECT * FROM {self.table_name} WHERE " + res)
            self.print(counter=1)
            logger.info("get succesful ")
        except psycopg2.errors.InvalidTextRepresentation:
            logger.error("get Error InvalidText")

    def update(self, per:Person , change:Person):
        """
        Изменение полей по параметру
        """
        try:
            res1 = change.request(',')
            logger.debug('request update get  = %s', res1)
            res2 = per.request('AND')
            logger.debug('request update change  = %s', res2)
            self.cursor.execute(f"UPDATE {self.table_name} SET {res1} WHERE {res2}")
            logger.info("update succesful ")
        except psycopg2.errors.UniqueViolation:
            logger.error("update Error : key is repeat")
        except psycopg2.errors.InvalidTextRepresentation:
            logger.error("update Error : InvalidText")
        self.connect.commit()

    def delete(self, per: Person):
        """
        Удаление строк
        """
        try:
            res = per.request('AND')
            logger.debug('request delete  = %s', res)
            self.cursor.execute(f"DELETE FROM {self.table_name} WHERE {res}")
            logger.info("delete succesful ")
        except psycopg2.errors.InvalidTextRepresentation:
            logger.error("delete Error: InvalidText ")
        self.connect.commit()


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

    def __del__(self):
        self.close()
        print('\n Соединение завершено')
