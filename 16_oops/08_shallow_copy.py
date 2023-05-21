# Import the copy module
from copy import *


# Declare a list -> Original list
original_list = [1, 2, [3, 4]]


# Shallow copy using copy() method
shallow_copy_list = original_list.copy()


# As not every object has .copy() method
# Shallow copy using copy module's copy function
shallow_copy_list = copy(original_list)


# Modify the original list
original_list[2][0] = 5


# Print the original list and shallow copy list
print(original_list)
print(shallow_copy_list)
