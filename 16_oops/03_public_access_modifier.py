# Create a class
class MyClass(object):
    # Constructor
    def __init__(self):
        # Public Variable
        self.public_var = 10

    # Public Method
    def public_method(self):
        print("This is public method")


# Create an instance of a class
obj = MyClass()


# Accessing public variable
print(obj.public_var)


# Calling public method
obj.public_method()
