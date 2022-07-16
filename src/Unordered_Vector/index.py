import numpy as np


class UnorderedVector:
    def __init__(self, size):
        self.size = size
        self.last_pos = -1
        self.values = np.empty(self.size, dtype=int)

    def __repr__(self):
        if self.last_pos == -1:
            return 'Empty array'
        else:
            value = '['
            for i in range(self.last_pos + 1):
                value += str(self.values[i])
                if i != self.last_pos:
                    value += ', '

            value += ']'
            return value

    def push(self, value):
        if self.last_pos == self.size - 1:
            print('Array full')
        else:
            self.last_pos += 1
            self.values[self.last_pos] = value
            
    def search(self, value):
        for i in range(self.last_pos + 1):
            if value == self.values[i]:
                return i
        return -1

    def delete(self, value):
        idx = self.search(value)

        if idx == -1:
            return

        print(idx, self.last_pos)
        for i in range(idx, self.last_pos):
            self.values[i] = self.values[i+1]

        self.last_pos -= 1


x = UnorderedVector(3)

x.push(51)

x.push(31)

x.delete(51)
print(x)
