# Import sys for system specific parameters and functions
import sys


# Declare an emtpy class
class EmptyClass(object):
    pass


# Create an instance of the EmptyClass
instance = EmptyClass()


# Calculate the memroy usage of the instance
memory_usage = sys.getsizeof(instance)


# Print the memory usage in bytes
print(f"Memory usage of an empty class instance: {memory_usage} bytes")
