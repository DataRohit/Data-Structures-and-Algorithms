# Take user input for number of rows
rows = int(input())


# Print pattern
"""
    1
    22
    333
    4444
    55555
"""
print("\nLeft half row number pyramid:")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()


# Print pattern
"""
    1
    23
    345
    4567
    56789
"""
print("\nLeft half row number start pyramid:")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(i + j - 1, end=" ")
    print()


# Print pattern
"""
    1
    21
    321
    4321
    54321
"""
print("\nLeft half reverse row number start pyramid:")
for i in range(1, rows + 1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
