# Parent class
class Animal(object):
    # Method
    def make_sounds(self):
        print("Generic animal sound.")


# Child class
class Dog(Animal):
    # Method overriding
    def make_sound(self):
        print("Woof!")


# Child class
class Cat(Animal):
    # Method overriding
    def make_sound(self):
        print("Meow!")


# Function to call the method from the object
def animal_sounds(animal):
    animal.make_sound()


# Create instance of the class
dog = Dog()
cat = Cat()


# Call the methods using the function
animal_sounds(dog)
animal_sounds(cat)
