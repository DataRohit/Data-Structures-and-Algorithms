# Function to return max frequency element
def maximumFrequency(arr):
    # Dict to store count of elements
    countDict = {}

    # Initialize maximum freq
    maxi = float("-inf")

    # Initialize answer element
    ans = None

    # Traverse the array
    for i in arr:
        # If element not in count dict
        if i not in countDict:
            # Create and entry in dict
            countDict[i] = 1

        # Else if element in count dict
        else:
            # Increment the counter
            countDict[i] += 1

        # If freq of current element > maximum freq
        # If first occurrence of current element < first occurrence of ans
        if countDict[i] > maxi or (
            countDict[i] == maxi and arr.index(i) < arr.index(ans)
        ):
            # Update maximum freq and answer element
            maxi = countDict[i]
            ans = i

    # Return the answer
    return ans


# Initialize list
arr = [1, 2, 2, 3, 1, 2]


# Print the answer
print(maximumFrequency(arr))
