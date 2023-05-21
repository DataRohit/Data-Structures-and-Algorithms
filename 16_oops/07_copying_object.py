# Create a class Person
class Person(object):
    # Constructor
    def __init__(self, name, age):
        # Initialize the class attributes
        self.name = name
        self.age = age

    # Change default string representation of object
    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"

    # Method to copy the current object to another variable
    def copy(self):
        return Person(self.name, self.age)


# Create a Person object
person1 = Person("John", 25)


# Create a copy of person1 using the copy method
person2 = person1.copy()


# Modify person2
person2.name = "Jane"
person2.age = 30


# Print both objects
print(person1)
print(person2)
