# Math for mathematical operations
from math import *


# Collections for deque
from collections import *


# Function to check if Person 1 knows Person 2
def knows(p1, p2, M):
    # If M[p1][p2] == 1
    if M[p1][p2] == 1:
        # p1 knows p2
        return True

    # Else return false
    return False


# Function to find if there is a celebrity in the party or not.
def find_celebrity(M, N):
    # Step 1
    # Initialize a stack
    # Add all people to stack
    s = [i for i in range(N)]

    # Step 2
    # Traverse the stack
    # Till size of stack is 1
    while len(s) != 1:
        # Get the top two people from the stack
        A = s.pop()
        B = s.pop()

        # If A knows B
        if knows(A, B, M):
            # Push B back to stack
            s.append(B)

        # If B knows A
        else:
            # Push A to stack
            s.append(A)

    # Step 3
    # Last person in stack is potential celebrity
    # Verify it

    # Row Checking
    row_check = False
    zero_count = 0

    # Traverse the respective row and count 0's
    for i in range(N):
        # If row element 0
        if M[s[-1]][i] == 0:
            # Update the zero count
            zero_count += 1

    # Check if all elements are 0
    if zero_count == N:
        # Update row_check
        row_check = True

    # Column Checking
    col_check = False
    one_count = 0

    # Traverse the respective col and count 1's
    for i in range(N):
        # If row element 1
        if M[i][s[-1]] == 1:
            # Update the one count
            one_count += 1

    # Check if all elements are 1
    if one_count == N - 1:
        # Update col_check
        col_check = True

    # If element is celebrity
    if row_check and col_check:
        # Return the element
        return s[-1]

    # Else return -1
    else:
        return -1


# User input for number of people at party
N = int(input())


# Initialize the matrix
M = []


# User input for matrix
for i in range(N):
    M.append(list(map(int, input().split())))


# Print the celebrity
print(find_celebrity(M, N))
