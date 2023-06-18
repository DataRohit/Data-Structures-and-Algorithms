# Function to check if current position is safe
def isSafe(row, col, occupiedRows, occupiedDiagonals, occupiedAntidiagonals):
    # If Queen not placed in row
    if row not in occupiedRows:
        # If Queen not placed in diagonal
        if (row + col) not in occupiedDiagonals:
            # If Queen not placed in antidiagonal
            if (row - col) not in occupiedAntidiagonals:
                # Position is safe
                return True

    # Else position is not safe
    return False


# Recursive function to get possible positions
def solve(col, n, board, occupiedRows, occupiedDiagonals, occupiedAntidiagonals, ans):
    # If queen placed in last column
    if col == n:
        # Add the board to ans
        ans.append([item for row in board for item in row])

        # Return to search for other possible boards
        return

    # Traverse over every row for column
    for row in range(n):
        # If current position is safe
        if isSafe(row, col, occupiedRows, occupiedDiagonals, occupiedAntidiagonals):
            # Place queen at the position
            board[row][col] = 1

            # Update the sets
            occupiedRows.add(row)
            occupiedDiagonals.add(row + col)
            occupiedAntidiagonals.add(row - col)

            # Recursive call for next column
            solve(
                col + 1,
                n,
                board,
                occupiedRows,
                occupiedDiagonals,
                occupiedAntidiagonals,
                ans,
            )

            # Backtrack and remove queen from current position
            board[row][col] = 0

            # Update the sets
            occupiedRows.remove(row)
            occupiedDiagonals.remove(row + col)
            occupiedAntidiagonals.remove(row - col)


# Function to return the boards with placed queens
def solveNQueens(n):
    # Initialize a board of size n x n
    board = [[0] * n for _ in range(n)]

    # Ans list to store all possible boards
    ans = []

    # Sets to store filled rows, diagonals and antidiagonals
    occupiedRows = set()
    occupiedDiagonals = set()
    occupiedAntidiagonals = set()

    # Call the recursive function to get possible boards with placed queens
    solve(0, n, board, occupiedRows, occupiedDiagonals, occupiedAntidiagonals, ans)

    # Return the answer list
    return ans


# Initialize n
n = 4


# Function call to get the boards with placed queens
ans = solveNQueens(n)


# Print the boards
for board in ans:
    for row in range(n):
        for col in range(n):
            print(board[row * n + col], end=" ")
        print()
    print()
