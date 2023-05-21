# Parent class
class Animal(object):
    # Constructor
    def __init__(self, name):
        self.name = name

    # Method
    def speak(self):
        print(f"{self.name} is making a sound.")


# Child class inheriting from Animal
class Dog(Animal):
    # Method
    def bark(self):
        print(f"{self.name} is barking.")


# Creating instances of the classes
animal = Animal("Generic Animal")
dog = Dog("Buddy")


# Calling the methods using the instances
animal.speak()
dog.speak()
dog.bark()
