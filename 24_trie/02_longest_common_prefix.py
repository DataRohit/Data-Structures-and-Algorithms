# Function to return the longest common prefix
def longestCommonPrefix(arr, n):
    # Answer string to store prefix
    ans = ""

    # Traverse every character of first word
    for i in range(len(arr[0])):
        # Access ith letter of first word
        ch = arr[0][i]

        # Initialize match to True
        match = True

        # Loop to traverse other words
        for j in range(1, n):
            # If the word not finished or
            # If character from first word does not match
            if len(arr[j]) < i or ch != arr[j][i]:
                # Set match to False
                match = False

                # Break the loop
                break

        # If not match
        if match == False:
            # Break the loop
            break

        # Update the answer check for next letter
        else:
            ans += ch

    # Return the answer
    return ans


# User input for array -> words
arr = ["coding", "codezen", "codingninja", "coder"]


# Function call
print(longestCommonPrefix(arr, len(arr)))
