# Parent class 1
class Mammal(object):
    # Method
    def breathe(self):
        print(f"{self.name} is breathing.")


# Parent class 2
class Animal(object):
    # Constructor
    def __init__(self, name):
        self.name = name

    # Method
    def speak(self):
        print(f"{self.name} is making a sound.")


# Child class inheriting from Mammal and Animal
class Dog(Mammal, Animal):
    # Method
    def bark(self):
        print(f"{self.name} is barking.")


# Creating an instance of the class
dog = Dog("Buddy")


# Call the methods using the instance
dog.breathe()
dog.speak()
dog.bark()
