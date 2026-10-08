from collections import deque

class MinStack:

    def __init__(self):
        # The main stack to hold all elements
        self.stack = deque()   
        # The extra stack to track the minimum element at each step
        self.min_stack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # If min_stack is empty, this val is the current minimum.
        # Otherwise, compare val with the top element of the min_stack.
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            current_min = min(val, self.min_stack[-1])
            self.min_stack.append(current_min)

    def pop(self) -> None:
        # Both stacks stay in sync, so pop from both
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # Peek at the rightmost (top) element of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Peek at the rightmost (top) element of the min_stack
        return self.min_stack[-1]
