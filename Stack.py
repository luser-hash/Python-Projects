"""
    Stack is a linear Data Structure that follows Last-In-First-Out or LIFO principle.
    That means the last element that added to the stack will remove first. 
    Stack operations:
        1. Push -> Add an element to the top of the stack.
        2. Pop -> Remove the top element from the stack.
        3. Peek ->  View the top element of the stack without removing it.
        4. isEmpty -> Check whether the stack is empty or not. 

    Examples of Stacks: 
        1. Undo / Redo in txt editors
        2. Browser history
"""


# Creating stack with OOP
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty."
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is empty."
        return self.stack[-1]
        
    def isEmpty(self):
        return len(self.stack) == 0
        
    def size(self):
        return len(self.stack)
    
mystack = Stack()

mystack.push(10)
mystack.push(20)
mystack.push(30)

print('Stack: ', mystack.stack)
print('Peek: ', mystack.peek())
print('Pop: ', mystack.pop())
print('isEmpty: ', mystack.isEmpty())
print('Size: ', mystack.size())


# Creating stack and it's operation without OOP

stack = []

# Push to stack
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)

# Pop element form stack
stack.pop()

# Peek of stack
peek = stack[-1]
print(peek)


# Is Empty -> check the len whether empty or not
isEmpty = not bool(len(stack))
print(isEmpty)