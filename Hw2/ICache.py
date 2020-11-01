class ICache:
    """
    sdvdsv
    """

    def __init__(self, capacity: int=10) -> None:
        """Инициализация класса"""
        self.keys = []
        self.mapping = {}
        self.capacity = capacity

    def get(self, key: str) -> str:
        """Метод получение значения"""
        try:
            value = self.mapping[key]
            return value
        except:
            print('')

    def set(self, key: str, value: str) -> None:
        """Метод заполнения"""
        if self.keys.count(key) == 0:
            self.keys.append(key)  # add key to end
        if len(self.keys) > self.capacity:
            _key = self.keys.pop(0)  # remove first key
            self.mapping.pop(_key)
        self.mapping[key] = value

    def delete(self, key: str) -> None:
        """Метод удаления"""
        self.mapping.pop(key)
        self.keys.remove(key)
