from ICache import ICache
from dict import MyDict

if __name__ == "__main__":


    a = MyDict([1, 2, 3])
    b = MyDict([1, 2,3,4,5,6,7,5])
    c = a + b
    d = a - b
    print(c)
    if c>d :
        print('ok sum>sub')
    if a == [1,2,3]:
        print ('ok ==')

    cache = ICache(100)
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.set('Jesse', 'James')
    cache.get('Jesse') # вернёт 'James'
    cache.delete('Walter')
    cache.get('Walter') # вернёт ''
    print("OK")