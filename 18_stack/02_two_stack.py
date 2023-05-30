class TwoStack:
    # Constructor
    def __init__(self, size):
        # Store the size of stack
        self.size = size

        # Initialize top's of the stacks
        self.top1 = -1
        self.top2 = size

        # Initialize stack to store elements
        self.stack = [None] * size

    # Push function for the first stack
    def push1(self, val):
        # Check if space is available for val
        if self.top1 < self.top2 - 1:
            # Increment top1
            self.top1 += 1

            # Insert the element
            self.stack[self.top1] = val
        else:
            print("Stack Overflow")

    # Push function for the second stack
    def push2(self, val):
        # Check if space is available for val
        if self.top1 < self.top2 - 1:
            # Decrement top2
            self.top2 -= 1

            # Insert the element
            self.stack[self.top2] = val
        else:
            print("Stack Overflow")

    # Pop function for the first stack
    def pop1(self):
        # If stack1 is underflow
        if self.top1 < 0:
            print("Stack 1 Underflow")
            return -1

        # If stack1 has elements
        else:
            # Remove the element
            ele = self.stack[self.top1]

            # Set the top to None
            self.stack[self.top1] = None

            # Decrement the top1
            self.top1 -= 1

            # Return popped element
            return ele

    # Pop function for the second stack
    def pop2(self):
        # If stack2 is underflow
        if self.top2 >= self.size:
            print("Stack 2 Underflow")
            return -1

        # If stack2 has elements
        else:
            # Remove the element
            ele = self.stack[self.top2]

            # Set the top to None
            self.stack[self.top2] = None

            # Increment the top2
            self.top2 += 1

            # Return popped element
            return ele


# Initialize a two stack
stack = TwoStack(6)


# Push elements into stack
stack.push1(1)
stack.push1(2)
stack.push1(3)

stack.push2(4)
stack.push2(5)
stack.push2(6)


# Print the stack
print(stack.stack)


# Pop elements from the stack 1
print(stack.pop1())


# Print the stack
print(stack.stack)


# Pop elements from the stack 2
print(stack.pop2())


# Print the stack
print(stack.stack)
