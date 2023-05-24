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


# Function to get the mid node
def get_mid(head):
    # Initialize slow and fast pointer
    slow_ptr = head
    fast_ptr = head

    # Traverse till fast pointer cannot move forward
    while fast_ptr.next is not None and fast_ptr.next.next is not None:
        # Update slow pointer by 1 node
        slow_ptr = slow_ptr.next

        # Update fast pointer by 1 node
        fast_ptr = fast_ptr.next

        # Check for 1 node after fast_ptr
        if fast_ptr.next is not None:
            fast_ptr = fast_ptr.next

    # Delete pointers
    del fast_ptr

    # Return the slow pointer -> mid node
    return slow_ptr


# Function to reverse the linked list
def reverse_linked_list(head):
    # Initialize prev and curr node
    prev_node = None
    curr_node = head

    # Loop curr_node is None -> prev_node at last node
    while curr_node is not None:
        # Store the next node for further reversing
        next_node = curr_node.next

        # Reverse the link
        curr_node.next = prev_node

        # Update the prev and curr node
        prev_node = curr_node
        curr_node = next_node

    # Delete the pointers
    del curr_node, next_node

    # Return the new head
    return prev_node


# Function to check for palindrome
def solve(head1, head2):
    # Initialize temp vars for traversing
    curr1 = head1
    curr2 = head2

    # Set default palindrome status
    palindrome = True

    # Loop till curr2 reaches the None
    # In case of odd nodes -> Ignore the middle node
    while curr2 is not None:
        # Compare data at curr1 and curr2
        if curr1.data != curr2.data:
            # Update palindrome
            palindrome = False

            # Break the loop

        # Move to next node
        curr1 = curr1.next
        curr2 = curr2.next

    # Return palindrome status
    return palindrome


# Function to check if linked list is palindrome
def check_palindrome(head):
    # Check if linked list is empty
    if head is None:
        return True

    # Check if linked list has only one element
    if head.next is None:
        return True

    # Call the function to get the middle node
    mid_ptr = get_mid(head)

    # Reverse the linked list after the mid_ptr
    new_head = reverse_linked_list(mid_ptr.next)

    # Connect the first and second half
    mid_ptr.next = new_head

    # Call the function to solve for palindrome
    return solve(head, new_head)


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
insert_at_tail(head_2, 3)
insert_at_tail(head_2, 2)
insert_at_tail(head_2, 1)


# Print linked list
print_linked_list(head_2)


# Check palindrome and print result
print(check_palindrome(head_2))
