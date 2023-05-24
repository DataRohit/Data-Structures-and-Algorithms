# Singly linked list class with a single head node
class SinglyLinkedList(object):
    # Constructor
    def __init__(self):
        """
        Initializes an empty singly linked list with empty head.
        """
        self.head = None

    # Method function to support iteration of linked list -> return the node at every iteration
    def __iter__(self):
        """
        Returns an iterator object for the singly linked list.

        Returns:
            An iterator object that allows iterating over the nodes of the linked list.
        """

        # Initialize starting node to head
        temp = self.head

        # Loop till we reach last node
        while temp:
            # Return the node as object
            yield temp

            # Move to next node
            temp = temp.next

        # Delete the temp variable
        del temp

    # Method function to support len function -> returns number of elements in linked list
    def __len__(self):
        """
        Returns the number of elements in the linked list.

        Returns:
            The number of elements in the linked list.
        """

        # Check if linked list is empty
        if self.head == None:
            return 0

        # Variable to track the length
        length = 1

        # Initialize temp with head for traversal
        temp = self.head

        # Traverse to find the last node
        while temp.next is not None:
            # Move to next node
            temp = temp.next

            # Update the length
            length += 1

        # Delete the temp variable
        del temp

        # Return the length
        return length

    # Class for node -> singly linked list node
    class Node(object):
        """
        Class for a node in the singly linked list.
        """

        # Constructor
        def __init__(self, data=None):
            """
            Initializes a node with the given data.

            Args:
                data: The data to be stored in the node.
            """
            self.data = data
            self.next = None

    # Method function to print the linked list
    def print_linked_list(self):
        """
        Prints the data of the linked list.
        """

        # Print the data of linked list in the form of list
        print([node.data for node in self])

    # Method function add new node at head
    def insert_at_head(self, data):
        """
        Inserts a new node with the given data at the head of the linked list.

        Args:
            data: The data to be inserted.
        """

        # If head is None
        if self.head == None:
            # Set the new node to head
            self.head = self.Node(data)

        # Else
        else:
            # Initialize a new node with new data
            temp = self.Node(data)

            # Add the new node at the start of linked list
            temp.next = self.head

            # Update the head
            self.head = temp

            # Delete the temp node
            del temp

    # Method function add new node at tail
    def insert_at_tail(self, data):
        """
        Inserts a new node with the given data at the tail of the linked list.

        Args:
            data: The data to be inserted.
        """

        # If head is None
        if self.head == None:
            # Set the new node to head
            self.head = self.Node(data)

        # Else
        else:
            # Initialize temp with head for traversal
            temp = self.head

            # Traverse to find the last node
            while temp.next is not None:
                # Move to next node
                temp = temp.next

            # Create a new node and add the node to the tail
            temp.next = self.Node(data)

            # Delete the temp variable
            del temp

    # Method function add new node at passed index
    def insert_at_index(self, data, index):
        """
        Inserts a new node with the given data at the specified index in the linked list.

        Args:
            data: The data to be inserted.
            index (int): The index at which the data should be inserted.

        Raises:
            ValueError: If the index is negative or out of range.
        """

        # Check for invalid index
        if index < 0:
            raise IndexError("Index should be >= 0")

        # If head is None
        if self.head == None:
            # Set the new node to head
            self.head = self.Node(data)

        # Else if index == 0 -> Insert at head
        elif index == 0:
            # Add the new data to head
            self.insert_at_head(data)

        # Else
        else:
            # Variables to store prev and next node
            prev_node = next_node = None

            # Traverse to find the nodes at index and index - 1
            for i, node in enumerate(self):
                # Stop if i == index
                if i == index:
                    break

                # Store the i - 1 and i index nodes
                prev_node = node
                next_node = node.next

            # Condition for index out of range
            if i < index:
                raise ValueError("Input index out of range")

            # Add the new node at index
            prev_node.next = self.Node(data)

            # Update the next node
            prev_node.next.next = next_node

            # Delete the pointers
            del prev_node, next_node

    # Method function delete node at head
    def delete_at_head(self):
        """
        Delete the node at the head of the linked list.

        Raises:
            ValueError: If the linked list is empty.
        """

        # If head is None
        if self.head == None:
            # Raise error
            raise ValueError("List is empty.")

        # Initialize temp with head
        temp = self.head

        # Update the head
        self.head = self.head.next

        # Delete temp
        del temp

    # Method function delete node at tail
    def delete_at_tail(self):
        """
        Delete the node at the tail of the linked list.

        Raises:
            ValueError: If the linked list is empty.
        """

        # If head is None
        if self.head == None:
            # Raise error
            raise ValueError("List is empty.")

        # If head is the only element
        elif self.head.next == None:
            # Set head to none
            self.head = None

        # Else
        else:
            # Initialize temp with head for traversal
            temp = self.head

            # Traverse to find the last node
            while temp.next.next is not None:
                # Move to next node
                temp = temp.next

            # Delete the last node
            del temp.next.next

            # Update the last node
            temp.next = None

            # Delete the temp variable
            del temp

    # Method function delete node at index
    def delete_at_index(self, index):
        """
        Deletes the node at the specified index.

        Parameters:
            index (int): The index of the node to be deleted.

        Raises:
            ValueError: If the list is empty or if the index is invalid.
        """

        # If head is None
        if self.head == None:
            # Raise error
            raise ValueError("List is empty.")

        # Check for invalid index
        if index < 0:
            raise IndexError("Index should be >= 0")

        # If index == 0 -> Delete head node
        elif index == 0:
            # Delete the head node
            self.delete_at_head()

        # Else
        else:
            # Initialize previous node to None
            prev_node = None

            # Initialize current node to head
            curr_node = self.head

            # Initialize variable to track index
            i = 0

            # Traverse to find the node at index - 1
            while curr_node is not None and i < index:
                # Update previous node and current node
                prev_node = curr_node
                curr_node = curr_node.next

                # Increment the counter
                i += 1

            # Check if current node is None
            if curr_node is None:
                raise ValueError("Input index out of range")

            # Point prev node to next node
            prev_node.next = curr_node.next

            # Delete the prev node and curr node
            del prev_node, curr_node

    # Method function delete first node with value
    def delete_by_value(self, data):
        """
        Deletes the first occurrence of node with specified value.

        Parameters:
            data: The data to be deleted.

        Raises:
            ValueError: If the list is empty or if the data is not found.
        """

        # If head is None
        if self.head == None:
            # Raise error
            raise ValueError("List is empty.")

        # Initialize previous node to None
        prev_node = None

        # Initialize current node to head
        curr_node = self.head

        # If element found at head
        if curr_node.data == data:
            # Delete head node
            self.delete_at_head()

        # Else
        else:
            # Traverse to find the node with specified value
            while curr_node is not None and curr_node.data != data:
                # Update previous node and current node
                prev_node = curr_node
                curr_node = curr_node.next

            # Check if current node is None -> Data not found
            if curr_node is None:
                raise ValueError("Input data not found.")

            # Else -> Data found
            else:
                # Point prev node to next node
                prev_node.next = curr_node.next

        # Delete the prev node and curr node
        del prev_node, curr_node

    # Method function update node at index
    def update_at_index(self, index, new_data):
        """
        Updates the node at the specified index.

        Parameters:
            index (int): The index of the node to be deleted.
            new_data: The data to be update.

        Raises:
            ValueError: If the list is empty or if the index is invalid.
        """

        # If head is None
        if self.head == None:
            # Raise error
            raise ValueError("List is empty.")

        # Check for invalid index
        if index < 0:
            raise IndexError("Index should be >= 0")

        # If index == 0 -> update head node
        elif index == 0:
            # Update value at head
            self.head.data = new_data

        # Else
        else:
            # Initialize current node to head
            curr_node = self.head

            # Initialize variable to track index
            i = 0

            # Traverse to find the node at index
            while curr_node is not None and i < index:
                # Update current node
                curr_node = curr_node.next

                # Increment the counter
                i += 1

            # Check if current node is None
            if curr_node is None:
                raise ValueError("Input index out of range")

            # Update curr node
            curr_node.data = new_data

            # Delete the curr node pointer
            del curr_node


# Doubly linked list class with a single head node
class DoublyLinkedList(object):
    # Constructor
    def __init__(self):
        """
        Initializes an empty doubly linked list with an empty head.
        """
        self.head = None

    # Method function to support iteration of linked list -> return the node at every iteration
    def __iter__(self):
        """
        Returns an iterator object for the doubly linked list.

        Returns:
            An iterator object that allows iterating over the nodes of the linked list.
        """

        # Initialize starting node to head
        temp = self.head

        # Loop till we reach last node
        while temp:
            # Return the node as object
            yield temp

            # Move to the next node
            temp = temp.next

        # Delete the temp variable
        del temp

    # Method function to support len function -> returns number of elements in linked list
    def __len__(self):
        """
        Returns the number of elements in the linked list.

        Returns:
            The number of elements in the linked list.
        """

        # Check if the linked list is empty
        if self.head is None:
            return 0

        # Variable to track the length
        length = 1

        # Initialize temp with head for traversal
        temp = self.head

        # Traverse to find the last node
        while temp.next is not None:
            # Move to the next node
            temp = temp.next

            # Update the length
            length += 1

        # Return the length
        return length

    # Class for a node in the doubly linked list.
    class Node(object):
        def __init__(self, data=None):
            """
            Initializes a node with the given data.

            Args:
                data: The data to be stored in the node.
            """
            self.data = data
            self.prev = None  # Reference to the previous node
            self.next = None  # Reference to the next node

    # Method function to print the linked list
    def print_linked_list(self):
        """
        Prints the data of the linked list.
        """

        # Print the data of linked list in the form of list
        print([node.data for node in self])

    # Method function add new node at head
    def insert_at_head(self, data):
        """
        Inserts a new node with the given data at the head of the linked list.

        Args:
            data: The data to be inserted.
        """

        # Create a new node with the given data
        new_node = self.Node(data)

        # If the list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
        else:
            # Set the new node's next reference to the current head
            new_node.next = self.head

            # Set the current head's previous reference to the new node
            self.head.prev = new_node

            # Update the head to the new node
            self.head = new_node

    # Method function add new node at tail
    def insert_at_tail(self, data):
        """
        Inserts a new node with the given data at the tail of the linked list.

        Args:
            data: The data to be inserted.
        """

        # Create a new node with the given data
        new_node = self.Node(data)

        # If the list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
        else:
            # Traverse to the last node
            node = self.head
            while node.next:
                node = node.next

            # Set the new node as the next node of the last node
            node.next = new_node

            # Set the last node as the previous node of the new node
            new_node.prev = node

    # Method function add new node at passed index
    def insert_at_index(self, data, index):
        """
        Inserts a new node with the given data at the specified index in the linked list.

        Args:
            data: The data to be inserted.
            index (int): The index at which the data should be inserted.

        Raises:
            ValueError: If the index is negative or out of range.
        """

        # Check for invalid index
        if index < 0:
            raise IndexError("Index should be >= 0")

        # If head is None
        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = self.Node(data)

        # Else if index == 0 -> Insert at head
        elif index == 0:
            # If index is 0, insert at the head
            self.insert_at_head(data)

        # Else
        else:
            # Variables to store nodes
            prev_node = None
            curr_node = self.head

            # Variable to track the index
            i = 0

            # Traverse to find the nodes
            while curr_node is not None and i < index:
                # Update the nodes
                prev_node = curr_node
                curr_node = curr_node.next

                # Update the index
                i += 1

            # Check if index is out of range
            if curr_node is None and i < index:
                # Index is out of range
                raise IndexError("Input index out of range")

            # Create a new node
            new_node = self.Node(data)

            # Update the links of the new node
            new_node.prev = prev_node
            new_node.next = curr_node

            # Update the links of the previous and current nodes
            prev_node.next = new_node

            if curr_node is not None:
                curr_node.prev = new_node

    # Method function delete node at head
    def delete_at_head(self):
        """
        Delete the node at the head of the linked list.

        Raises:
            ValueError: If the linked list is empty.
        """

        # If head is None
        if self.head is None:
            raise ValueError("List is empty.")

        # Initialize temp with head
        temp = self.head

        # Update the head
        if self.head.next is not None:
            self.head.next.prev = None

        self.head = self.head.next

        # Delete temp
        del temp

    # Method function delete node at tail
    def delete_at_tail(self):
        """
        Delete the node at the tail of the linked list.

        Raises:
            ValueError: If the linked list is empty.
        """

        # If head is None
        if self.head is None:
            raise ValueError("List is empty.")

        # If head is the only element
        if self.head.next is None:
            # If head is the only element
            del self.head
            self.head = None

        # Else
        else:
            # Traverse to find the last node
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            # Update the links of the last and second last nodes
            temp.prev.next = None

            # Delete the temp variable
            del temp

    # Method function delete node at index
    def delete_at_index(self, index):
        """
        Deletes the node at the specified index.

        Parameters:
            index (int): The index of the node to be deleted.

        Raises:
            ValueError: If the list is empty or if the index is invalid.
        """

        # If head is None
        if self.head is None:
            raise ValueError("List is empty.")

        # Check for invalid index
        if index < 0:
            raise IndexError("Index should be >= 0")

        # If index == 0 -> Delete head node
        if index == 0:
            # Delete the head node
            self.delete_at_head()

        # Else
        else:
            # Initialize previous node and current node
            prev_node = None
            curr_node = self.head

            # Initialize the variable to track index
            i = 0

            # Traverse to find the node
            while curr_node is not None and i < index:
                # Update the prev and curr node
                prev_node = curr_node
                curr_node = curr_node.next

                # Update the index pointer
                i += 1

            # Check if current node is None
            if curr_node is None:
                raise ValueError("Input index out of range")

            # Update the links of the previous and next nodes
            prev_node.next = curr_node.next

            if curr_node.next is not None:
                curr_node.next.prev = prev_node

            # Delete the prev node and curr node
            del prev_node, curr_node

    # Method function delete first node with value
    def delete_by_value(self, data):
        """
        Deletes the first occurrence of node with specified value.

        Parameters:
            data: The data to be deleted.

        Raises:
            ValueError: If the list is empty or if the data is not found.
        """

        # If head is None
        if self.head is None:
            raise ValueError("List is empty.")

        # Initialize current node
        curr_node = self.head

        # If element found at head
        if curr_node.data == data:
            # Delete head
            self.delete_at_head()

        # Else
        else:
            # Traverse to find the node with specified value
            while curr_node is not None and curr_node.data != data:
                curr_node = curr_node.next

            # Check if current node is None -> Data not found
            if curr_node is None:
                raise ValueError("Input data not found.")

            # Else -> Data found
            else:
                # Update the links of the previous and next nodes
                curr_node.prev.next = curr_node.next

                if curr_node.next is not None:
                    curr_node.next.prev = curr_node.prev

            # Delete the prev node and curr node
            del curr_node

    # Method function update node at index
    def update_at_index(self, index, new_data):
        """
        Updates the node at the specified index.

        Parameters:
            index (int): The index of the node to be updated.
            new_data: The data to be updated.

        Raises:
            ValueError: If the list is empty or if the index is invalid.
        """

        # If head is None
        if self.head is None:
            raise ValueError("List is empty.")

        # Check for invalid index
        if index < 0:
            raise IndexError("Index should be >= 0")

        # If index == 0 -> update head node
        if index == 0:
            # Update the value at the head node
            self.head.data = new_data

        # Else
        else:
            # Initialize current node to head
            curr_node = self.head

            # Initialize variable to track index
            i = 0

            # Traverse to find the node at index
            while curr_node is not None and i < index:
                # Update current node
                curr_node = curr_node.next

                # Increment the counter
                i += 1

            # Check if current node is None
            if curr_node is None:
                raise ValueError("Input index out of range")

            # Update curr node
            curr_node.data = new_data

        # Delete the curr node pointer
        del curr_node


# Circular singly linked list class with a single head node
class SinglyCircularLinkedList:
    """
    SinglyCircularLinkedList class represents a singly circular linked list.
    """

    def __init__(self):
        """
        Initialize an empty singly circular linked list.
        """
        self.head = None

    def __iter__(self):
        """
        Support iteration over the linked list.
        """
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.head:
                break

    def __len__(self):
        """
        Return the length of the linked list.
        """
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
            if node == self.head:
                break
        return length

    class Node:
        """
        Node class represents a node in a singly circular linked list.
        """

        def __init__(self, data):
            """
            Initialize a new node with the given data.

            Args:
                data: The data to be stored in the node.
            """
            self.data = data
            self.next = None

    def print_linked_list(self):
        """
        Prints the data of the linked list.
        """

        # Print the data of linked list in the form of list
        print([node.data for node in self])

    def insert_at_head(self, data):
        """
        Insert a new node with the given data at the head of the linked list.

        Args:
            data: The data to be inserted at the head.
        """
        new_node = self.Node(data)
        if not self.head:
            # If the linked list is empty, set the new node as the head
            # and make it point to itself.
            self.head = new_node
            new_node.next = self.head
        else:
            # Find the last node and make it point to the new node.
            # Update the head to the new node.
            current = self.head
            while current.next != None and current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_at_tail(self, data):
        """
        Insert a new node with the given data at the tail of the linked list.

        Args:
            data: The data to be inserted at the tail.
        """
        new_node = self.Node(data)
        if not self.head:
            # If the linked list is empty, set the new node as the head
            # and make it point to itself.
            self.head = new_node
            new_node.next = self.head
        else:
            # Check if head is only node
            if self.head.next is None:
                self.head.next = new_node
                new_node.next = self.head

            # Else
            else:
                # Find the last node and make it point to the new node.
                current = self.head

                while current.next != self.head:
                    current = current.next

                current.next = new_node
                new_node.next = self.head

    def insert_at_index(self, data, index):
        """
        Insert a new node with the given data at the specified index of the linked list.

        Args:
            data: The data to be inserted.
            index: The index at which the data should be inserted.
        """
        if index < 0 or index > len(self):
            raise IndexError("Index out of range.")

        if index == 0:
            # If the index is 0, insert the node at the head.
            self.insert_at_head(data)
        elif index == len(self):
            # If the index is equal to the length of the linked list,
            # insert the node at the tail.
            self.insert_at_tail(data)
        else:
            # Find the node at the previous index and insert the new node after it.
            new_node = self.Node(data)
            current = self.head
            count = 0
            while count < index - 1:
                current = current.next
                count += 1
            new_node.next = current.next
            current.next = new_node

    def delete_at_head(self):
        """
        Delete the node at the head of the linked list.
        """
        if not self.head:
            # Raise error
            raise ValueError("List is empty.")

        if self.head.next == self.head:
            # If there is only one node in the linked list,
            # set the head to None.
            self.head = None
        else:
            # Find the last node and make it point to the node
            # after the head. Update the head to the next node.
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next

    def delete_at_tail(self):
        """
        Delete the node at the tail of the linked list.
        """
        if not self.head:
            # Raise error
            raise ValueError("List is empty.")

        if self.head.next == self.head:
            # If there is only one node in the linked list,
            # set the head to None.
            self.head = None
        else:
            # Find the second-to-last node and make it point
            # to the head. Update the last node to None.
            current = self.head
            while current.next.next != self.head:
                current = current.next
            current.next = self.head

    def delete_at_index(self, index):
        """
        Delete the node at the specified index of the linked list.

        Args:
            index: The index of the node to be deleted.
        """
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range.")

        if index == 0:
            # If the index is 0, delete the node at the head.
            self.delete_at_head()
        elif index == len(self) - 1:
            # If the index is equal to the length of the linked list minus 1,
            # delete the node at the tail.
            self.delete_at_tail()
        else:
            # Find the node at the previous index and delete the next node.
            current = self.head
            count = 0
            while count < index - 1:
                current = current.next
                count += 1
            current.next = current.next.next

    def delete_by_value(self, value):
        """
        Delete the node with the specified value from the linked list.

        Args:
            value: The value of the node to be deleted.
        """
        if not self.head:
            # Raise error
            raise ValueError("List is empty.")

        if self.head.data == value:
            # If the value is found at the head, delete the node at the head.
            self.delete_at_head()
        else:
            # Find the node with the specified value and delete it.
            current = self.head
            while current.next != self.head:
                if current.next.data == value:
                    current.next = current.next.next
                    return
                current = current.next

        print("Value not found in the linked list.")

    def update_at_index(self, index, data):
        """
        Update the value of the node at the specified index of the linked list.

        Args:
            index: The index of the node to be updated.
            data: The new data value.
        """
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range.")

        current = self.head
        count = 0
        while count < index:
            current = current.next
            count += 1
        current.data = data


# Circular doubly linked list class with a single head node
class DoublyCircularLinkedList:
    """
    Represents a doubly circular linked list.
    """

    def __init__(self):
        """
        Initialize an empty doubly circular linked list.
        """
        self.head = None
        self.tail = None

    def __iter__(self):
        """
        Enable iteration over the doubly circular linked list.
        """
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.head:
                break

    def __len__(self):
        """
        Returns the number of nodes in the doubly circular linked list.
        """
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
            if node == self.head:
                break
        return count

    class Node:
        """
        Represents a node in a doubly circular linked list.
        """

        def __init__(self, data):
            """
            Initialize a node with the given data.

            Args:
                data: The data to be stored in the node.
            """
            self.data = data
            self.prev = None
            self.next = None

    def print_linked_list(self):
        """
        Prints the data of the linked list.
        """

        # Print the data of linked list in the form of list
        print([node.data for node in self])

    def insert_at_head(self, data):
        """
        Insert a new node with the given data at the head of the doubly circular linked list.

        Args:
            data: The data to be inserted.
        """
        new_node = self.Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node

    def insert_at_tail(self, data):
        """
        Insert a new node with the given data at the tail of the doubly circular linked list.

        Args:
            data: The data to be inserted.
        """
        new_node = self.Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_index(self, data, index):
        """
        Insert a new node with the given data at the specified index in the doubly circular linked list.

        Args:
            data: The data to be inserted.
            index: The index at which the new node should be inserted.
        """
        if index < 0 or index > len(self):
            raise IndexError("Index out of range")

        if index == 0:  # If inserting at the head
            self.insert_at_head(data)
            return

        if index == len(self):  # If inserting at the tail
            self.insert_at_tail(data)
            return

        new_node = self.Node(data)
        node = self.head
        for _ in range(index - 1):
            node = node.next

        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def delete_at_head(self):
        """
        Delete the node at the head of the doubly circular linked list.
        """
        if not self.head:  # If the list is empty
            # Raise error
            raise ValueError("List is empty.")

        if self.head == self.tail:  # If there's only one node in the list
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head

    def delete_at_tail(self):
        """
        Delete the node at the tail of the doubly circular linked list.
        """
        if not self.head:  # If the list is empty
            # Raise error
            raise ValueError("List is empty.")

        if self.head == self.tail:  # If there's only one node in the list
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail

    def delete_at_index(self, index):
        """
        Delete the node at the specified index in the doubly circular linked list.

        Args:
            index: The index of the node to be deleted.
        """
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")

        if index == 0:  # If deleting the head
            self.delete_at_head()

        elif index == len(self) - 1:  # If deleting the tail
            self.delete_at_tail()

        else:
            node = self.head
            for _ in range(index):
                node = node.next

            node.prev.next = node.next
            node.next.prev = node.prev

    def delete_by_value(self, value):
        """
        Delete the first occurrence of a node with the given value from the doubly circular linked list.

        Args:
            value: The value of the node to be deleted.
        """
        if not self.head:  # If the list is empty
            # Raise error
            raise ValueError("List is empty.")

        elif self.head.data == value:  # If deleting the head
            self.delete_at_head()

        else:
            node = self.head.next
            while node != self.head:
                if node.data == value:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    break
                else:
                    node = node.next

            else:
                raise ValueError("Input data not found.")

    def update_at_index(self, index, data):
        """
        Update the data of the node at the specified index in the doubly circular linked list.

        Args:
            index: The index of the node to be updated.
            data: The new data value.
        """
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")

        node = self.head
        for _ in range(index):
            node = node.next

        node.data = data
