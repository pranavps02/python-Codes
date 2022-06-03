from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def printArea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 8

    def printArea(self):
        return  + self.length * self.breadth

class Square(Shape):
    type = "Square"
    sides = 4

    def __init__(self):
        self.side = 10

    def printArea(self):
        return self.side * self.side


rect = Rectangle()
sqa = Square()

print(rect.printArea())
print(sqa.printArea())