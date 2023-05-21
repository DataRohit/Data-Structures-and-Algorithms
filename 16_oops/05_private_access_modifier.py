# Create a class
class MyClass(object):
    # Constructor
    def __init__(self):
        # Private Variable
        self.__protected_var = 10

    # Private Method
    def __private_method(self):
        print("This is private method")


# Create an instance of a class
obj = MyClass()


# Accessing private variable
print(obj.__protected_var)


# Calling private method
obj.__private_method()


# Results in an AttributeError: 'MyClass' object has no attribute '__private_var'
# Results in an AttributeError: 'MyClass' object has no attribute '__private_method'
