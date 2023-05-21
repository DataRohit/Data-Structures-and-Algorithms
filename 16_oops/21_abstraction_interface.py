# Parent class
class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement 'speak' method.")


# Child class
class Dog(Animal):
    def speak(self):
        return "Woof!"


# Child class
class Cat(Animal):
    def speak(self):
        return "Meow!"


# Create an instance and call the method
dog = Dog()
print(dog.speak())


# Create an instance and call the method
cat = Cat()
print(cat.speak())  # Output: Meow!
