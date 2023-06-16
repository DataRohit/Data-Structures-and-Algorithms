# Class to represent a Trie node
class TrieNode(object):
    def __init__(self, char):
        # Initialize the node with a character and an empty children array
        self.char = char

        # Each node has 26 children, one for each letter of the alphabet
        self.children = [None] * 26

        # isTerminal is True if the node represents end of a word
        self.isTerminal = False


# Class to implement a Trie
class Trie(object):
    # Constructor
    def __init__(self):
        # Initialize the Trie root node with an empty character
        self.root = TrieNode("")

    # Helper recursive function to insert a new word to the Trie
    def __insertUtil(self, root, word):
        # Base case -> Empty word
        if len(word) == 0:
            # Mark the current node as a leaf node
            root.isTerminal = True

            # Return
            return

        # Get the index of the character
        index = ord(word[0]) - ord("A")

        # If the node does not exist, create a new node
        if root.children[index] is None:
            root.children[index] = TrieNode(word[0])

        # Recursively insert the remaining word
        self.__insertUtil(root.children[index], word[1:])

    # Method to insert a new word to the Trie
    def insertWord(self, word):
        # Convert word to uppercase
        word = word.upper()

        # Call the helper recursive function to insert the word
        self.__insertUtil(self.root, word)

    # Helper recursive function to search for a word in the Trie
    def __searchUtil(self, root, word):
        # Base case -> Empty word
        if len(word) == 0:
            # Return True if the current node is a leaf node
            return root.isTerminal

        # Get the index of the character
        index = ord(word[0]) - ord("A")

        # If the node does not exist, return False
        if root.children[index] is None:
            return False

        # Recursively search for the remaining word
        return self.__searchUtil(root.children[index], word[1:])

    # Method to search for a word in the Trie
    def searchWord(self, word):
        # Convert word to uppercase
        word = word.upper()

        # Call the helper recursive function to search for the word
        return self.__searchUtil(self.root, word)

    # Helper recursive function to delete a word from the Trie
    def __deleteUtil(self, root, word):
        # Base case -> Empty word
        if len(word) == 0:
            # If the current node is not a leaf node, return False
            if not root.isTerminal:
                return False

            # Mark the current node as a non-leaf node
            root.isTerminal = False

            # If the current node has no children, return True
            if root.children.count(None) == len(root.children):
                return True

            # Else, return False
            return False

        # Get the index of the character
        index = ord(word[0]) - ord("A")

        # If the node does not exist, return False
        if root.children[index] is None:
            return False

        # Recursively delete the remaining word
        return self.__deleteUtil(root.children[index], word[1:])

    # Method to delete a word from the Trie
    def deleteWord(self, word):
        # Convert word to uppercase
        word = word.upper()

        # Call the helper recursive function to delete the word
        return self.__deleteUtil(self.root, word)


# Create a Trie
trie = Trie()


# Insert some more words
trie.insertWord("Hello")
trie.insertWord("Hell")
trie.insertWord("Hells")
trie.insertWord("Help")
trie.insertWord("Helps")


# Search for words
print(trie.searchWord("Hello"))  # True
print(trie.searchWord("Hell"))  # True
print(trie.searchWord("Hells"))  # True
print(trie.searchWord("Help"))  # True
print(trie.searchWord("Helps"))  # True
print(trie.searchWord("Helll"))  # False
print(trie.searchWord("Hel"))  # False


# Delete some words
print(trie.deleteWord("Hello"))  # True


# Search for words
print(trie.searchWord("Hello"))  # False
