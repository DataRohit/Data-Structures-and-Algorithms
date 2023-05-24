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


# Function to merge the values
def add(first, second):
    # Pointers to track the lists
    curr1 = first
    curr2 = second

    # Ans linked list to store the answer
    ans_rev_head = Node(-1)
    ans_rev_tail = ans_rev_head

    # Variable to track the carry value
    carry = 0

    # Traverse until the largest number is finished
    while curr1 is not None or curr2 is not None:
        # Get the value from the node
        # If node is none use 0
        val1 = curr1.data if curr1 is not None else 0
        val2 = curr2.data if curr2 is not None else 0

        # Get the addition of the current nodes values and carry
        num = val1 + val2 + carry

        # Get the remainder to add to the answer
        remainder = num % 10

        # Get the quotient to update the carry
        carry = num // 10

        # Add remainder to the ans_rev linked list
        ans_rev_tail.next = Node(remainder)

        # Update the tail
        ans_rev_tail = ans_rev_tail.next

        # Update curr1 and curr2 pointers if they are not None
        if curr1 is not None:
            curr1 = curr1.next
        if curr2 is not None:
            curr2 = curr2.next

    # If there is still a carry left, add it to the answer
    if carry > 0:
        ans_rev_tail.next = Node(carry)

    # Delete variables
    del curr1, curr2, ans_rev_tail, carry, val1, val2, num, remainder

    # Return the ans_rev linked list
    return ans_rev_head.next


# Function to add the two linked list
def add_two_list(first, second):
    # Reverse both the linked list
    first_rev = reverse_linked_list(first)
    second_rev = reverse_linked_list(second)

    # Call the merge function to return the new head
    ans_head = reverse_linked_list(add(first_rev, second_rev))

    print_linked_list(ans_head)


# Initialize number 1
first = Node(4)
insert_at_tail(first, 5)


# Initialize number 2
second = Node(3)
insert_at_tail(second, 4)
insert_at_tail(second, 5)


add_two_list(first, second)
