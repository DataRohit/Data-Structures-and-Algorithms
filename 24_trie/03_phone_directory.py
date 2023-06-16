class TrieNode:
    def __init__(self):
        # Flag to track if node is a terminal node
        self.isEnd = False

        # Dictionary to store the children nodes
        self.children = {}


class Trie:
    def __init__(self):
        # Initialize the root node of the Trie
        self.root = TrieNode()

    def insert(self, string):
        # Get the length of the input string
        n = len(string)

        # Start traversing the Trie from the root node
        itr = self.root

        # Traverse over the characters in the input string
        for i in range(n):
            # If the current character is not in the children of the current node
            if string[i] not in itr.children:
                # Create a new node for the current character
                itr.children[string[i]] = TrieNode()

            # Move to the next node
            itr = itr.children[string[i]]

        # Mark the last node as a terminal node
        itr.isEnd = True

    def viewSuggestionsHelper(self, curr, prefix, temp):
        # If the current node is a terminal node, add the prefix to the temporary list
        if curr.isEnd:
            temp.append(prefix)

        # Iterate over all possible characters
        c = ord("a")

        while c <= ord("z"):
            # If the character is in the children of the current node
            if chr(c) in curr.children:
                # Get the next node
                next_node = curr.children[chr(c)]

                # Recursively call the helper function with the next node
                self.viewSuggestionsHelper(next_node, prefix + chr(c), temp)

            # Move to the next character
            c += 1

    def viewSuggestions(self, string):
        # Start with the root node
        prev = self.root

        # Initialize an empty prefix string
        prefix = ""

        # Get the length of the input string
        n = len(string)

        # Initialize a list to store the result suggestions
        result = []

        # Initialize a pointer for traversal
        i = 0

        # Traverse the input string
        while i < n:
            # Update the prefix with the next character
            prefix += string[i]

            # Get the last entered character
            lastCharacter = prefix[i]

            # If the last character is not in the children of the previous node
            if lastCharacter not in prev.children:
                # Increment the pointer and break the loop
                i += 1

                break

            # Update the current node to the node corresponding to the last character
            curr = prev.children[lastCharacter]

            # Create a temporary list to store suggestions for the current prefix
            temp = []

            # Call the recursive helper function to populate the temporary list
            self.viewSuggestionsHelper(curr, prefix, temp)

            # Add the temporary list to the result list
            result.append(temp)

            # Update the previous node to the current node
            prev = curr

            # Increment the pointer
            i += 1

        # Return the final result
        return result


def phoneDirectory(contactList, queryStr):
    # Create a Trie instance
    trie = Trie()

    # Insert all the contacts into the Trie
    for contact in contactList:
        trie.insert(contact)

    # Return the suggestions for the query string
    return trie.viewSuggestions(queryStr)


# Initialize a list of contacts
contactList = [
    "contact",
    "code",
    "coder",
    "coding",
    "codingminutes",
    "codingsimplified",
]


# Initialize the query string
queryStr = "cod"


# Function call
for i in phoneDirectory(contactList, queryStr):
    print(i)
