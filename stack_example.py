# Create a Stack class and its methods

# We will first - Define the class
class Stack:

    # This init method allows us to use a Python list 
    def __init__(self):
        self.item = [] #initialize an empty list


    # Use Push function to add an item to the stack 
    def push(self, item):
        self.item.append(item) #Use append to add the item 


    # Use the built in Pop method to remove items from the stack which automatically returns the last item of the list
    def pop(self):
        pass


    # We can peek what the next item is going to be removed
    def peek(self):
        pass

    # Use size to know how many items are in the stack
    def size(self):
        pass

    # Check if the stack is empty
    def is_empty(self):
        pass

# Push
new_stack = Stack()
new_stack.push('Money')
new_stack.push('Stack')

print(new_stack)
