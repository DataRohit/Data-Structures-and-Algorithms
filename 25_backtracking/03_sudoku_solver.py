# Function to check if passed coordinates are safe to insert the passed value
def isSafe(board, n, row, col, val):
    # Check in row and column
    for i in range(n):
        if board[row][i] == val or board[i][col] == val:
            return False

    # Check in 3x3 matrix
    startRow = 3 * (row // 3)
    startCol = 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[startRow + i][startCol + j] == val:
                return False

    return True


# Recursive function to solve the sudoku
def solve(board):
    # Find the size of the grid
    n = len(board)

    # Loop for rows
    for row in range(n):
        # Loop for columns
        for col in range(n):
            # If position is empty
            if board[row][col] == 0:
                # Loop over possible values
                for val in range(1, 10):
                    # If val can be placed at the current position
                    if isSafe(board, n, row, col, val):
                        # Place the value
                        board[row][col] = val

                        # If solution is possible for the updated board
                        if solve(board):
                            return True

                        # If no solution is possible with the current value, backtrack
                        board[row][col] = 0

                # No solution found for the current position
                return False

    # Board completed
    return True


# Function to return the solved sudoku
def solveSudoku(sudoku):
    # Call the recursive solve function
    solve(sudoku)


# Initialize a sudoku board with some empty positions
sudoku = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]


# Call the function to solve the sudoku
solveSudoku(sudoku)


# Print the solved sudoku
for row in sudoku:
    print(*row)
