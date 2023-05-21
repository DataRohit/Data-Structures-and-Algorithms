# Parent class
class Animal(object):
    # Constructor
    def __init__(self, name) -> None:
        self.name = name

    # Method
    def speak(self):
        print(f"{self.name} is making a sound.")


# Child class 1 inheriting from Animal
class Dog(Animal):
    # Method
    def bark(self):
        print(f"{self.name} is barking.")


# Child class 2 inheriting from Animal
class Cat(Animal):
    # Method
    def purr(self):
        print(f"{self.name} is purring.")


# Creating instance of the classes
dog = Dog("Buddy")
cat = Cat("Kitty")


# Call the methods using the instances
dog.speak()
dog.bark()

cat.speak()
cat.purr()
