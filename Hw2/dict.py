class MyDict(list):


    def __add__(self: list, other: list) -> list:
        min_len = min(len(self), len(other))
        max_len = max(len(self), len(other))

        result = MyDict()

        for i in range(min_len):
            result.append(self[i] + other[i])

        for i in range(min_len, max_len):
            if max_len == len(self):
                result.append(self[i])
            else:
                result.append(other[i])

        return result

    def __sub__(self: list, other: list) -> list:
        min_len = min(len(self), len(other))
        max_len = max(len(self), len(other))

        result = MyDict()

        for i in range(min_len):
            result.append(self[i] - other[i])

        for i in range(min_len, max_len):
            if max_len == len(self):
                result.append(self[i])
            else:
                result.append(0 - other[i])

        return result

    def __lt__(self: list, other: list) -> bool:
        return sum(self) < sum(other)

    def __le__(self: list, other: list) -> bool:
        return sum(self) <= sum(other)

    def __eq__(self: list, other: list) -> bool:
        return sum(self) == sum(other)

    def __ne__(self: list, other: list) -> bool:
        return sum(self) != sum(other)

    def __gt__(self: list, other: list) -> bool:
        return sum(self) > sum(other)

    def __ge__(self: list, other: list) -> bool:
        return sum(self) >= sum(other)
