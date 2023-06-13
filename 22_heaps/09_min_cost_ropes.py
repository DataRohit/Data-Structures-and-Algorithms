# Import heapq
from heapq import *


# Function to return the minimum cost
def connectRopes(arr):
    # Convert arr to min heap
    heapify(arr)

    # Initialize cost
    cost = 0

    # Traverse till only element remains in min heap
    while len(arr) > 1:
        # Pop the two smallest element
        a = heappop(arr)
        b = heappop(arr)

        # Get the sum
        currCost = a + b

        # Increment the cost
        cost += currCost

        # Push the currCost to min heap
        heappush(arr, currCost)

    # Return the final cost
    return cost


# Initialize list with length of ropes
arr = [1, 2, 3, 4, 5]


# Call the function
print(connectRopes(arr))
