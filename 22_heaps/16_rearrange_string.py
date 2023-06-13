# Import heapq
import heapq


# Function to rearrange the characters in a string such that no two adjacent characters are the same
def reArrangeString(S):
    # Step 1: Count the frequency of each character in the input string S
    char_freq = {}
    for char in S:
        char_freq[char] = char_freq.get(char, 0) + 1

    # Step 2: Create a max-heap to store (-frequency, character) tuples
    heap = [(-freq, char) for char, freq in char_freq.items()]
    heapq.heapify(heap)

    # Step 3: Initialize variables
    result = []  # List to store the rearranged string
    prev_char = None  # Variable to keep track of the previous character

    # Step 4: Process the heap until it is empty
    while heap:
        # Step 4.1: Pop the character with the highest frequency from the heap
        neg_freq, char = heapq.heappop(heap)

        # Step 4.2: Check if the character is different from the previous character
        if prev_char != char:
            # Append the character to the result
            result.append(char)

            # Decrease the frequency by 1 and push the character back into the heap if necessary
            if neg_freq < -1:
                heapq.heappush(heap, (neg_freq + 1, char))

            # Update the previous character
            prev_char = char

        # Step 4.3: If the character is the same as the previous character, select a different character
        else:
            # If the heap is empty, it means no other characters are available, so rearrangement is not possible
            if not heap:
                return "not possible"

            # Pop another character from the heap
            neg_freq2, char2 = heapq.heappop(heap)

            # Append the different character to the result
            result.append(char2)

            # Decrease the frequency by 1 and push the character back into the heap if necessary
            if neg_freq2 < -1:
                heapq.heappush(heap, (neg_freq2 + 1, char2))

            # Push the original character and its updated frequency back into the heap
            heapq.heappush(heap, (neg_freq, char))

            # Update the previous character
            prev_char = char2

    # Step 5: Return the rearranged string by joining the characters in the result list
    return "".join(result)


# Take user input for the string
S = input()


# Call the function to rearrange the characters in the string
result = reArrangeString(S)


# Display the rearranged string
print(result)
