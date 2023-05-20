# Import typing for type hinting
from typing import *


# Recursive function to get total ways to climb stairs
def ways_to_climb_stairs(n: int) -> int:
    # If stair number < 0 -> 0 ways possible
    if n < 0:
        return 0

    # If stair number  == 0 -> 1 way only
    if n == 0:
        return 1

    # If stairs > 0
    return ways_to_climb_stairs(n - 1) + ways_to_climb_stairs(n - 2)


# Take user input for total stairs
n = int(input())


# Call the function and print the total ways to climb stairs
print(ways_to_climb_stairs(n))
