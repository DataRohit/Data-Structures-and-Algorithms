# Function to check presence of permutation of s1 in s2
def check_inclusion(s1: str, s2: str) -> bool:
    # Array to store the count of s1 elements
    count1 = [0] * 26

    # Loop over s1 elements
    for i in range(len(s1)):
        # Update the count of character
        count1[ord(s1[i]) - ord("a")] += 1

    # Sliding window traversal of s2 string
    i = 0
    window_size = len(s1)

    # Array to store the count character in window
    count2 = [0] * 26

    # Check for first window
    while i < window_size and i < len(s2):
        # Update the count
        count2[ord(s2[i]) - ord("a")] += 1

        # Update i counter
        i += 1

    # If count1 == count2
    if count1 == count2:
        # Return true
        return True

    # Traverse further
    while i < len(s2):
        # Update the count of new element in count 2
        count2[ord(s2[i]) - ord("a")] += 1

        # Decrement the count of element to be removed
        count2[ord(s2[i - window_size]) - ord("a")] -= 1

        # Update i pointer
        i += 1

        # If count1 == count2
        if count1 == count2:
            # Return true
            return True

    # No permutation exist
    return False


# Take input for strings
s1, s2 = map(str, input().split())


# Call the function and check if any permutation of s1 is in s2
print(check_inclusion(s1, s2))
