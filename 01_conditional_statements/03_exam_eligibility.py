# Function to check exam eligibility
def check_exam_eligible(a, n):
    # Calculate percentage and return
    return (a / n) * 100 >= 75


# Take user input for total and attended classes
a, n = map(int, input().split())

# Print the exam eligibility
print(check_exam_eligible(a, n))
