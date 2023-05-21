# Declare the class
class MyClass:
    # Constructor
    def __init__(self, name):
        # Attribute
        self.name = name

        # Print the message
        print(f"Creating an instance of MyClass with name {self.name}")

    # Overriding the del method
    def __del__(self):
        # Print the message at deletion
        print(f"Destroying the instance of MyClass with name {self.name}")


# Creating objects of MyClass
obj1 = MyClass("Object 1")
obj2 = MyClass("Object 2")


# Deleting objects explicitly
del obj1
del obj2
