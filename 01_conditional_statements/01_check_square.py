# Function to check square
def check_square(l, b):
    # Return true if square
    if l == b and l > 0 and b > 0:
        return True

    # Else return false
    else:
        return False


# Function to get the perimeter
def get_perimeter(l, b):
    # Check if l and b are +ve
    if l > 0 and b > 0:
        # Calculate and return perimeter
        return 2 * (l + b)

    else:
        # Else return -1
        return -1


# Function to get the area
def get_area(l, b):
    # Check if l and b are +ve
    if l > 0 and b > 0:
        # Calculate and return the area
        return l * b

    else:
        # Else return -1
        return -1


# Take user input for l and b
l, b = map(float, input().split())

# Check if square
print(check_square(l, b))

# Print perimeter
print(get_perimeter(l, b))

# Print area
print(get_area(l, b))
