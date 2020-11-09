import logging
from orm import MyOrm, Person

if __name__ == "__main__":
    logging.basicConfig(filename="logInfo.log",level=logging.DEBUG, filemode='w')
    logging.info("Program started")
    a = MyOrm()

    a.create(Person(name="qwert",age=1454, email="qweqwr@mail",phone=9969234123))
    a.create(Person(id = 13,name="Arseny",age=13, email="qweqwr@mail"))
    a.create(Person(id =13))
    a.create(Person(id="sdgfsdg"))
    a.create(Person(id=13, name = "ssdgsadgsd"))
    a.create(Person( name="Arseny", age=1454, email="111111@mail"))
    a.create(Person(name="Arseny", age=1454, email="aaaaaa@mail"))
    a.get_all()
    a.get(Person(age=1454))
    a.update(Person(name="Arseny"),Person(id = 666 , name = 'Maxim',age = 666))
    a.update(Person(name="qwert"), Person( name='Maxim', age=666))
    a.get_all()
    a.drop()
    logging.info("Done!")