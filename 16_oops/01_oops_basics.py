# Import sys for system specific parameters and functions
import sys


# Create a class representing a Car
class Car(object):
    # Constructor function
    def __init__(self, make, model, year):
        # Print the value of self
        print(self)

        # Set attributes of the class
        self.make = make
        self.model = model
        self.year = year

    # Method 1
    def start_engine(self):
        print("The engine is running.")

    # Method 2
    def stop_engine(self):
        print("The engine is stopped.")


# Create and Initialize an object of the class
my_car = Car("Toyota", "fortuner", 2021)


# Calculate the memory usage of the instance
memory_usage = sys.getsizeof(my_car)


# Print the memory usage in bytes
print(f"Memory usage of an instance: {memory_usage} bytes")


# Access the attributes of the object using dot notation
print(my_car.make)
print(my_car.model)
print(my_car.year)


# Call the methods of the object using dot notation
my_car.start_engine()
my_car.stop_engine()
