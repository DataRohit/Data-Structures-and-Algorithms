# Function to check leap year
def check_leap_year(year):
    # If leap year
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        # Return true
        return True
    else:
        # Else return false
        return False


# User input for year
year = int(input())

# Check and print the result
print(check_leap_year(year))
