import numpy as np


class OrderedVector:
    def __init__(self, size):
        self.last_pos = -1
        self.size = size
        self.values = np.empty(self.size, dtype=int)

    def __repr__(self):
        if self.last_pos == -1:
            return 'Empty array'

        value = '['
        for i in range(self.last_pos + 1):
            value += str(self.values[i])
            if i != self.last_pos:
                value += ', '

        value += ']'
        return value


x = OrderedVector(3)


print(x)
