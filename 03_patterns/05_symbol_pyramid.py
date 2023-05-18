# Take user input for number of rows
rows = int(input())


# Print pattern
"""
    +
    + +
    + + +
    + + + +
    + + + + +
"""
print("\nLeft bottom half star pyramid:")
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if i >= j:
            print("+", end=" ")
        else:
            print("  ", end="")
    print()


# Print pattern
"""
            +
          + + 
        + + +
      + + + + 
    + + + + +
"""
print("\nRight bottom half star pyramid:")
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if i + j >= rows + 1:
            print("+", end=" ")
        else:
            print("  ", end="")
    print()


# Print pattern
"""
    + + + + +
    + + + + 
    + + +
    + +
    +
"""
print("\nLeft top half star pyramid:")
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if i + j >= rows + 2:
            print("  ", end="")
        else:
            print("+", end=" ")
    print()


# Print pattern
"""
    + + + + +
      + + + +
        + + +
          + +
            +
"""
print("\nRight top half star pyramid:")
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if i >= j + 1:
            print("  ", end="")
        else:
            print("+", end=" ")
    print()
