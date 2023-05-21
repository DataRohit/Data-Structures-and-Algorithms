# Declare the class
class MyClass:
    # Class attribute
    static_attribute = 10

    # Constructor
    def __init__(self, x):
        self.x = x

    # Instance method
    def instance_method(self):
        # Accessing the instance attribute 'x'
        print(f"Instance attribute 'x': {self.x}")

        # Accessing the class attribute 'static_attribute'
        print(f"Class attribute 'static_attribute': {MyClass.static_attribute}")

    # Static method
    @staticmethod
    def static_method():
        # Static methods don't have access to instance attributes or methods.
        # They can only access class attributes.
        print(f"Static method accessing class attribute 'static_attribute': {MyClass.static_attribute}")


# Creating instances of MyClass
obj1 = MyClass(5)
obj2 = MyClass(7)


# Accessing instance methods and attributes
obj1.instance_method()  # Instance attribute 'x': 5, Class attribute 'static_attribute': 10
obj2.instance_method()  # Instance attribute 'x': 7, Class attribute 'static_attribute': 10


# Accessing the static attribute directly using the class name
print(f"Accessing class attribute 'static_attribute' directly: {MyClass.static_attribute}")  # 10


# Accessing the static attribute using an instance
print(f"Accessing class attribute 'static_attribute' using an instance: {obj1.static_attribute}")  # 10


# Accessing the static method using the class name
MyClass.static_method()  # Static method accessing class attribute 'static_attribute': 10


# Accessing the static method using an instance
obj1.static_method()  # Static method accessing class attribute 'static_attribute': 10
