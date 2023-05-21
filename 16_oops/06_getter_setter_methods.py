# Declare a class
class MyClass:
    # Constructor
    def __init__(self):
        # Attributes
        self._my_attribute = None

    # Getter method -> Method to get the attribute value from the object
    @property
    def my_attribute(self):
        return self._my_attribute

    # Setter method -> Method to set the attribute value into the object
    @my_attribute.setter
    def my_attribute(self, value):
        self._my_attribute = value


# Create an instance of the class
obj = MyClass()


# Getter Method -> Before Setter Method
print(obj.my_attribute)


# Use Setter Method
obj.my_attribute = 42


# Getter Method -> After Setter Method
print(obj.my_attribute)
