# Import collection for using deque
from collections import deque


# Function to get the first non-repeating character in stream
def first_non_repeating(A):
    # Initialize a dictionary to store count of character
    count_dict = {}

    # Initialize an empty queue
    queue = deque()

    # Initialize answer string
    ans = ""

    # Traverse the input string
    for char in A:
        # If char is repeating
        if char in count_dict.keys():
            # Update the count
            count_dict[char] += 1

        # Char not in dictionary
        else:
            # Add char to count_dict
            count_dict[char] = 1

        # Add element to queue
        queue.append(char)

        # Loop till queue is empty
        while len(queue) > 0:
            # If front element is repeating character
            if count_dict[queue[0]] > 1:
                # Pop the element
                queue.popleft()

            # Else front element is non-repeating character
            else:
                # Add element to answer
                ans += queue[0]

                # Break the loop
                break

        # If queue is empty
        if len(queue) == 0:
            ans += "#"

    # Return ans
    return ans


# User input for string
A = input()


# Print the first non-repeating character in stream
print(first_non_repeating(A))
