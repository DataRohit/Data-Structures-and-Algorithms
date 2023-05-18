# Take user input for number of rows
rows = int(input())


# Print pattern
"""
       1
      121
     12321
    1234321
"""
print("\nNumbers full pyramid:")
for i in range(1, rows + 1):
    for j in range(rows - i, -1, -1):
        print("  ", end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(1, rows):
        if i > j:
            print(i - j, end=" ")
    print()


# Print pattern
"""
    12344321
    123**321
    12****21
    1******1
"""
print("\nNumbers and star full pyramid:")
for i in range(rows, 0, -1):
    for j in range(1, rows + 1):
        if i >= j:
            print(j, end=" ")
        else:
            print("*", end=" ")

    for j in range(rows, 0, -1):
        if i >= j:
            print(j, end=" ")
        else:
            print("*", end=" ")

    print()
