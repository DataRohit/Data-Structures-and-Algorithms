# Initialize and unordered map
unorderedMap = {}


# Add elements to the unordered map
unorderedMap["a"] = 1
unorderedMap["b"] = 2
unorderedMap["c"] = 3
unorderedMap["d"] = 4
unorderedMap["e"] = 5


# Print the unordered map
print("Unordered Map \t->", unorderedMap)


# Print the size of the unordered map
print("Length \t\t->", len(unorderedMap))


# Get the value of a key
print("a \t\t->", unorderedMap["a"])


# Accessing a key that does not exist
# NOTE: Prefer using the get() method to avoid errors
# print("f ->", unorderedMap["f"])  # KeyError: 'f'
print("f \t\t->", unorderedMap.get("f"))  # None


# Check if a key exists
print("a in map \t->", "a" in unorderedMap)


# Delete a key
del unorderedMap["a"]


# Print the unordered map
print("Unordered Map \t->", unorderedMap)


# Use setdefault() to set a default value for a key
# If key not exist create a new key with the default value
print("f \t\t->", unorderedMap.setdefault("f", 6))


# Print the unordered map
print("Unordered Map \t->", unorderedMap)


# Access keys using setdefault()
# If key exist return the value of the key
print("c \t\t->", unorderedMap.setdefault("c", 7))


# Traverse the unordered map
print("\nTraverse")
for key, value in unorderedMap.items():
    print(key, "->", value)
