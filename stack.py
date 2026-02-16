#!/usr/bin/env python3
"""
Stack Implementation in Python
A stack is a LIFO (Last In First Out) data structure.
"""

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add an item to the top of the stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item from the stack"""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        """Return the top item without removing it"""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]
    
    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the stack"""
        return len(self.items)
    
    def clear(self):
        """Remove all items from the stack"""
        self.items = []
    
    def __str__(self):
        return f"Stack({self.items})"
    
    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    # Test the Stack implementation
    stack = Stack()
    
    print("Pushing elements: 1, 2, 3, 4, 5")
    for i in range(1, 6):
        stack.push(i)
        print(f"Pushed {i}, stack: {stack}")
    
    print(f"\nStack size: {stack.size()}")
    print(f"Top element (peek): {stack.peek()}")
    
    print("\nPopping elements:")
    while not stack.is_empty():
        popped = stack.pop()
        print(f"Popped: {popped}, remaining stack: {stack}")
    
    print(f"\nIs stack empty? {stack.is_empty()}")
