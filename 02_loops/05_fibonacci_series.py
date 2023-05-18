# Function to print fibonacci series
def print_fibonacci_series(vals):
    # Initialize starting two values
    a, b = 0, 1

    # Check if vals < 2
    if vals < 2:
        # Print error
        print("Error")
    else:
        # Print first two elements
        print(a, end=" ")
        print(b, end=" ")

        # Check if vals > 2
        if vals > 2:
            # Loop for vals times
            for i in range(2, vals):
                # Update the elements
                a, b = b, a + b

                # Print the element
                print(b, end=" ")


# Take user input for number of elements to view
vals = int(input())

# Call the function to print fibonacci series
print_fibonacci_series(vals)
