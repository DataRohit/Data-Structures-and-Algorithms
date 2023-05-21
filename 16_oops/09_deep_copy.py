# Import the copy module
from copy import *


# Declare a list -> Original list
original_list = [1, 2, [3, 4]]


# Deep copy using copy module's deepcopy function
shallow_copy_list = deepcopy(original_list)


# Modify the original list
original_list[2][0] = 5


# Print the original list and deep copy list
print(original_list)
print(shallow_copy_list)
