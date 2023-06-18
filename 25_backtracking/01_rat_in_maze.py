# Function to check if passed coordinates are safe or not
def isSafe(newX, newY, arr, n, visited):
    # Check if newX and newY are within the range
    if 0 <= newX < n and 0 <= newY < n:
        # Check if the new position is not blocked and not visited
        if arr[newX][newY] != 0 and not visited[newX][newY]:
            return True

    # Not safe position to move
    return False


# Recursive function to find paths
def solve(x, y, arr, n, ans, visited, path):
    # Base case -> Destination reached
    if x == n - 1 and y == n - 1:
        # Add the path to the answer list
        ans.append(path)

        # Return to search for other alternate path
        return

    # Mark the current position as visited
    visited[x][y] = True

    # Possible movements: D (down), L (left), R (right), U (up)

    # Check if down movement is safe
    if isSafe(x + 1, y, arr, n, visited):
        # Recursive call for the next down block
        solve(x + 1, y, arr, n, ans, visited, path + "D")

    # Check if left movement is safe
    if isSafe(x, y - 1, arr, n, visited):
        # Recursive call for the next left block
        solve(x, y - 1, arr, n, ans, visited, path + "L")

    # Check if right movement is safe
    if isSafe(x, y + 1, arr, n, visited):
        # Recursive call for the next right block
        solve(x, y + 1, arr, n, ans, visited, path + "R")

    # Check if up movement is safe
    if isSafe(x - 1, y, arr, n, visited):
        # Recursive call for the next up block
        solve(x - 1, y, arr, n, ans, visited, path + "U")

    # Backtrack and mark the current position as not visited
    visited[x][y] = False


# Function to return the paths from start to end
def searchMaze(arr, n):
    # List to store all possible paths
    ans = []

    # Initialize a 2D visited array of size n x n
    visited = [[False] * n for _ in range(n)]

    # If starting position is blocked
    if arr[0][0] == 0:
        # Return an empty list
        return ans

    # Call the recursive function to get all possible paths
    solve(0, 0, arr, n, ans, visited, "")

    # Return the answer list
    return ans


# Input maze
maze = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]


# Get all possible paths
paths = searchMaze(maze, len(maze))


# Print all possible paths
print(paths)
