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


# Function to return the merged linked list
def merge_two_list(head_1, head_2):
    # If first list is empty
    if head_1 is None:
        # Return second list
        return head_2

    # If second list is empty
    if head_2 is None:
        # Return first list
        return head_1

    # Create a node to store new head
    new_head = Node(-1)
    new_tail = new_head

    # Pointer to track first and second list
    curr_1 = head_1
    curr_2 = head_2

    # Loop till either of the list is finished
    while curr_1 is not None and curr_2 is not None:
        # If curr_1 data <= curr_2 data
        if curr_1.data <= curr_2.data:
            # Add curr_1 to new head
            new_tail.next = curr_1

            # Update curr_1
            curr_1 = curr_1.next

        # If curr_1 data > curr_2 data
        else:
            # Add curr_2 to new head
            new_tail.next = curr_2

            # Update curr_2
            curr_2 = curr_2.next

        # Update the new_tail
        new_tail = new_tail.next

    # If first list is remaining
    if curr_1 is not None:
        new_tail.next = curr_1

    # If second list is remaining
    if curr_2 is not None:
        new_tail.next = curr_2

    # Delete pointers
    del curr_1, curr_2, new_tail

    # Return the new head
    return new_head.next


# Initialize first linked list
head_1 = Node(1)
insert_at_tail(head_1, 4)
insert_at_tail(head_1, 5)


# Initialize second linked list
head_2 = Node(2)
insert_at_tail(head_2, 3)
insert_at_tail(head_2, 5)


# Print the linked list
print_linked_list(head_1)
print_linked_list(head_2)


# Call the function to get the merged linked list
new_head = merge_two_list(head_1, head_2)


# Print new linked list
print_linked_list(new_head)


print_linked_list(head_1)
print_linked_list(head_2)
