from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        return 1

    def __iter__(self):
        return iter((self.a, self.b, self.c))

# s = Shape()
t = Triangle(1, 2, 3)

for i in t:
    print(i)

from random import shuffle

lst = [[1, 2], [0, 5]]
shuffle(lst)
print(sorted(lst, key=lambda x: x[0]))
