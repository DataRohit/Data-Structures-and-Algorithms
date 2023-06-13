# Import the heapq library
import heapq


# Function to invert the sign of each element in the list
def invertSign(my_list):
    return [-x for x in my_list]


# Initialize a list
my_list = [21, 1, 45, 78, 3, 5]


# Convert all elements to negative
my_list = invertSign(my_list)


# Print the original list
print(invertSign(my_list))


# Use heapify to rearrange the elements
heapq.heapify(my_list)


# Print the heap
print(invertSign(my_list))


# Use heappush to insert a new element
heapq.heappush(my_list, -8)


# Print the modified heap
print(invertSign(my_list))


# Use heappop to pop the largest element
largest = heapq.heappop(my_list)


# Print the popped element and the modified heap
print(-largest, invertSign(my_list))


# Use heappushpop to push and pop elements simultaneously
print(-heapq.heappushpop(my_list, -6), invertSign(my_list))


# Use heapreplace to pop and push elements
# Pop and print the largest element
print(-heapq.heapreplace(my_list, -17), invertSign(my_list))
