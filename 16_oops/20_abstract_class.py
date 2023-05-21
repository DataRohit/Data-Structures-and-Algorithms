# Import abstract base class
from abc import ABC, abstractmethod


# Abstract class "Shape"
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Derived class "Rectangle"
class Rectangle(Shape):
    def __init__(self, length, breadth) -> None:
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


# Create an instance of the class
rect = Rectangle(5, 3)


# Call the methods
print(rect.area())
print(rect.perimeter())
