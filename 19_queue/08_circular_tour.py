def circular_tour(petrol, distance, N):
    # Variable to track extra required petrol
    deficit = 0

    # Variable to track the balance petrol
    balance = 0

    # Initialize the starting index
    start = 0

    # Traverse the petrol and distance list
    for i in range(N):
        # Update the balance
        balance += petrol[i] - distance[i]

        # If balance is negative
        if balance < 0:
            # Update the deficit
            deficit += balance

            # Update the starting point
            start = i + 1

            # Reset balance
            balance = 0

    # If the balance petrol + required >= 0
    if deficit + balance >= 0:
        # Return the start
        return start

    # Travel not possible
    else:
        return -1


# Take user input for number of petrol pumps
N = int(input())


# Take user input for petrol
petrol = list(map(int, input().split()))[:N]


# Take user input for distance
distance = list(map(int, input().split()))[:N]


# Call the function to find the starting point
print(circular_tour(petrol, distance, N))
