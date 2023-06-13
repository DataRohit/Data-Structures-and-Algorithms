# Import the heapq library
import heapq


# Initialize a list
my_list = [21, 1, 45, 78, 3, 5]


# Print the original list
print(my_list)


# Use heapify to rearrange the elements
heapq.heapify(my_list)


# Print the heap
print(my_list)


# Use heappush to insert a new element
heapq.heappush(my_list, 8)


# Print the modified heap
print(my_list)


# Use heappop to pop the smallest element
smallest = heapq.heappop(my_list)


# Print the popped element and the modified heap
print(smallest, my_list)


# Use heappushpop to push and pop elements simultaneously
print(heapq.heappushpop(my_list, 6), my_list)


# Use heapreplace to pop and push elements
# Pop and print the smallest element
print(heapq.heapreplace(my_list, 17), my_list)
