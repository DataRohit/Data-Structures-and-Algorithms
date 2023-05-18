# Function to calculate the bonus amount
def calculate_bonus(salary, service):
    # Check if service > 5 years and salary > 0
    if service >= 5 and salary > 0:
        # Calculate and return bonus
        return salary * 0.05

    else:
        # No bonus
        return -1


# Take user input for salary and service
salary, service = map(float, input().split())

# Print the result
print(calculate_bonus(salary, service))
