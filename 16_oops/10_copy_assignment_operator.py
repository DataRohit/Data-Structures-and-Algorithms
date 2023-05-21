# Import the copy module
from copy import *


# Declare the class
class MyClass(object):
    # Constructor
    def __init__(self, value):
        # Attribute
        self.value = value

    # Copy assignment function
    def __copy__(self):
        # Create a new object with the same value
        new_obj = MyClass(self.value)

        # Return the shallow copy of the object
        return new_obj

    # Deep copy assignment function
    def __deepcopy__(self, memo):
        # Deep copy the value
        new_obj = MyClass(deepcopy(self.value, memo))

        # Return the deep copy of the object
        return new_obj


# Create an object
obj1 = MyClass(10)


# Use the copy assignment operator
obj2 = obj1


# Use the deepcopy assignment operator
obj3 = deepcopy(obj1)


# Modify the value of obj2
obj2.value = 20


# Check the value of obj1
print(obj1.value)


# Check the value of obj2
print(obj2.value)


# Check the value of obj3
print(obj3.value)
