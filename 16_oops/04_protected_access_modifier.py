# Create a class
class MyClass(object):
    # Constructor
    def __init__(self):
        # Protected Variable
        self._protected_var = 10

    # Protected Method
    def _protected_method(self):
        print("This is protected method")


# Create a subclass
class SubClass(MyClass):
    # Constructor
    def __init__(self):
        # Inheriting from parent class
        super().__init__()

    # Method to access the protected member
    def access_protected_member(self):
        # Accessing protected variable
        print(self._protected_var)

        # Calling protected methods
        self._protected_method()


# Create an instance of the sub class
obj = SubClass()


# Accessing the protected member using the sub class
obj.access_protected_member()
