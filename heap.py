#!/usr/bin/env python3
"""
Heap (Min Heap) Implementation in Python
A heap is a complete binary tree that satisfies the heap property.
"""

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, value):
        """Insert a new value into the heap"""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, i):
        """Move the element up to maintain heap property"""
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    
    def extract_min(self):
        """Remove and return the minimum element (root)"""
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_val
    
    def _heapify_down(self, i):
        """Move the element down to maintain heap property"""
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
        
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right
        
        if i != min_index:
            self.swap(i, min_index)
            self._heapify_down(min_index)
    
    def peek(self):
        """Return the minimum element without removing it"""
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]
    
    def size(self):
        """Return the number of elements in the heap"""
        return len(self.heap)
    
    def is_empty(self):
        """Check if the heap is empty"""
        return len(self.heap) == 0
    
    def __str__(self):
        return str(self.heap)


if __name__ == "__main__":
    # Test the MinHeap implementation
    heap = MinHeap()
    
    print("Inserting elements: 5, 3, 8, 1, 9, 2")
    for val in [5, 3, 8, 1, 9, 2]:
        heap.insert(val)
    
    print(f"Heap after insertions: {heap}")
    print(f"Minimum element (peek): {heap.peek()}")
    
    print("\nExtracting elements in sorted order:")
    while not heap.is_empty():
        print(f"Extracted: {heap.extract_min()}")
