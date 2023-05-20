# Import typing for type hinting
from typing import *


# Function to check if the direction is safe to move
def is_safe(x: int, y: int, n: int, visited: List[List[int]], m: List[List[int]]) -> bool:
    # Condition 1 -> new x and y are in matrix and cell not visited and path is open
    if (x >= 0 and x < n) and (y >= 0 and y < n) and (visited[x][y] == 0) and (m[x][y] == 1):
        # Cell is safe to move
        return True

    # Else cell is not safe to move
    return False


# Function to get the possbile direction for the rat to move
def solve(m: List[List[int]], n: int, ans: List[str], x: int, y: int, visited: List[List[int]], path: str) -> None:
    # Base case -> destination reached
    if x == n - 1 and y == n - 1:
        # Add path to answer
        ans.append(path)

        # Return return
        return

    # Set the visited cell
    visited[x][y] = 1

    # Define the directions the rat can move (up, down, left, right)
    directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    # Try all possible directions
    for letter, direction in directions.items():
        # Get the update x and y cordinates
        newx = x + direction[0]
        newy = y + direction[1]

        # Check direction
        if is_safe(newx, newy, n, visited, m):
            # If path is safe add to path
            path += letter

            # Recursive call for checking and solving
            solve(m, n, ans, newx, newy, visited, path)

            # Backtrack and remove D from path
            path = path[:-1]

    # Backtrack visited cell
    visited[x][y] = 0


# Main function to find the path from source to destination
def find_path(m: List[List[int]], n: int) -> List[str]:
    # Initialize answer array to store total the path
    ans = []

    # Check if source cell is blocked
    if m[0][0] == 0:
        # Return empty matrix
        return ans

    # Initialize and declare the start index in the matrix
    srcx, srcy = 0, 0

    # Array to keep track of the visisted cells
    visited = [[0] * n for _ in range(n)]

    # String to track the path
    path = ""

    # Call the solve function to get the possible path
    solve(m, n, ans, srcx, srcy, visited, path)

    # Sort the ans array
    ans.sort()

    # Return the answer array
    return ans


# Take user input for rows and columns
n = int(input())


# Initialize the matrix
matrix = [0] * n


# Loop for rows
for j in range(n):
    # Initialize array of size n with 0
    arr = [0] * n

    # Array input
    arr_input = input()

    # Loop over index
    for index, k in enumerate(arr_input.split()):
        # Break if index >= n
        if index >= n:
            # Break out of loop
            break

        # Get user input
        arr[index] = int(k)

    # Add row to matrix
    matrix[j] = arr


# Call the find path function and print the possbile path
print(find_path(matrix, n))
