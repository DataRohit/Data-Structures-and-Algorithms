# Class for node -> singly linked list node
class Node(object):
    # Constructor
    def __init__(self, data=None):
        self.data = data
        self.next = None


# Function to print linked list
def print_linked_list(head):
    # Temp node to traverse
    temp = head

    # Traverse till last node
    while temp is not None:
        # Print the node value
        print(temp.data, end=" ")

        # Move to next node
        temp = temp.next

    # Add line break
    print()


# Function to add node to tail
def insert_at_tail(head, data):
    # If head is None
    if head == None:
        # Set the new node to head
        head = Node(data)

    # Else
    else:
        # Initialize temp with head for traversal
        temp = head

        # Traverse to find the last node
        while temp.next is not None:
            # Move to next node
            temp = temp.next

        # Create a new node and add the node to the tail
        temp.next = Node(data)

        # Delete the temp variable
        del temp


# Function to check if linked list is palindrome
def check_palindrome(head):
    # Create an empty list to store the linked list data
    data_list = []

    # Temp node for traversing the linked list
    curr = head

    # Traverse the linked list
    while curr is not None:
        # Add the data to data_list
        data_list.append(curr.data)

        # Update the current node
        curr = curr.next

    # Check for palindrome
    return data_list == data_list[::-1]


# Initialize first linked list
head_1 = Node(1)
insert_at_tail(head_1, 2)
insert_at_tail(head_1, 3)
insert_at_tail(head_1, 4)
insert_at_tail(head_1, 5)
insert_at_tail(head_1, 6)


# Print linked list
print_linked_list(head_1)


# Check palindrome and print result
print(check_palindrome(head_1))


# Initialize second linked list
head_2 = Node(1)
insert_at_tail(head_2, 2)
insert_at_tail(head_2, 1)


# Print linked list
print_linked_list(head_2)


# Check palindrome and print result
print(check_palindrome(head_2))
