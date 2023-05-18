# Input for rows and columns
rows, cols = map(int, input().split())


# Loop to print the pattern using row number
"""
    1   1   1   1   1   1
    2   2   2   2   2   2
    3   3   3   3   3   3
"""
print("\nPattern using row number:")
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        print(i, end="\t")
    print()


# Loop to print the pattern using col number
"""
    1   2   3   4   5   6
    1   2   3   4   5   6
    1   2   3   4   5   6
"""
print("\nPattern using col number:")
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        print(j, end="\t")
    print()


# Loop to print the pattern using reverse col number
"""
    6   5   4   3   2   1
    6   5   4   3   2   1
    6   5   4   3   2   1
"""
print("\nPattern using reverse col number:")
for i in range(1, rows + 1):
    for j in range(cols, 0, -1):
        print(j, end="\t")
    print()


# Loop to print the pattern using counting number
"""
    1   2   3   4   5   6
    7   8   9   10  11  12
    13  14  15  16  17  18
"""
print("\nPattern using counting number:")
count = 1
for i in range(1, rows + 1):
    for j in range(cols, 0, -1):
        print(count, end="\t")
        count += 1
    print()
