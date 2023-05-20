# Import typing for type hinting
from typing import *


# Function to calculate the power
def power(n: int, p: int) -> int:
    # Base case for power is 0
    if p == 0:
        return 1

    # Base case for power is 1
    if p == 1:
        return n

    # Recursive case for power
    ans = power(n, p // 2)

    # If b is even
    if p % 2 == 0:
        return ans * ans

    # If b is odd
    else:
        return n * ans * ans


# Take user input for number and power
n, p = map(int, input().split())


# Call the function and get the power
print(power(n, p))
