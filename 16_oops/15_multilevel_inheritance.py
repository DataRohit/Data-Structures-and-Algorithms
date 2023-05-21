# Grandparent class
class Animal(object):
    # Constructor
    def __init__(self, name):
        self.name = name

    # Method
    def speak(self):
        print(f"{self.name} is making a sound.")


# Parent class inheriting from Animal
class Mammal(Animal):
    # Method
    def breathe(self):
        print(f"{self.name} is breathing.")


# Child class inheriting from Mammal
class Dog(Mammal):
    # Method
    def bark(self):
        print(f"{self.name} is barking.")


# Creating an instance of the class
dog = Dog("Buddy")


# Calling the methods using the instance
dog.speak()
dog.breathe()
dog.bark()
