# Take user input for rows and cols
rows, cols = map(int, input().split())


# Print pattern
"""
    AAAAA
    BBBBB
    CCCCC
"""
print("\nRow square pattern:")
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        print(chr(ord("A") + i - 1), end=" ")
    print()


# Print pattern
"""
    ABCDE
    ABCDE
    ABCDE
"""
print("\nColumn square pattern:")
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        print(chr(ord("A") + j - 1), end=" ")
    print()


# Print pattern
"""
    ABC
    DEF
    GHI
"""
print("\nSequence square pattern:")
val = ord("A")
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        print(chr(val), end=" ")
        val += 1
    print()


# Print pattern
"""
    ABC
    BCD
    CDE
"""
print("\nRow start square pattern:")
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        print(chr(ord("A") + i + j - 2), end=" ")
    print()
