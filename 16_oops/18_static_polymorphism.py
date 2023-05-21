# Declare the class
class MyClass(object):
    # Method
    def my_method(self, x=None):
        # If x does not exist
        if x is None:
            # Default behavior
            print("No argument provided.")

        # If x exist
        else:
            # Custom behavior
            print(f"Argument provided: {x}")


# Create an instance of the class
obj = MyClass()


# Call the method without and with parameters
obj.my_method()
obj.my_method(10)
