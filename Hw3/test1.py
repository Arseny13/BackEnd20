import logging
from test import orm, Person

if __name__ == "__main__":
    logging.basicConfig(filename="logInfo1.log", level=logging.DEBUG, filemode='w')
    logging.info("Program started")
    A =Person('main')
    A.create(name = "Arseny")
    A.create(age=13)
    A.all()
    A.delete(name = 'Arseny')
    A.create(name = 'qwert',age=13)
    A.create(name='QQQQ', age=13)
    A.create(name='ASS', age=13)
    B = A.get(age=13,name = 'ASS')
    B.save(age = 666)
    B.all()
    A.all()

    B.drop()
    A.drop()
