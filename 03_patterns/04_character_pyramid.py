# Take user input for number of rows
rows = int(input())


# Print pattern
"""
    A
    BC
    CDE
    DEFG
"""
print("\nSequence left half pyramid:")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(chr(ord("A") + i + j - 2), end=" ")
    print()


# Print pattern
"""
    D
    CD
    BCD
    ABCD
"""
print("\nLeft half reverse row number start pyramid:")
for i in range(rows, 0, -1):
    for j in range(1, rows - i + 2):
        print(chr(ord("A") + i + j - 2), end=" ")
    print()
