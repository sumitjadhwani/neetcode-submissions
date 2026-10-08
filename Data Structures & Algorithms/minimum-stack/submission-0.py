from collections import deque

class MinStack:

    def __init__(self):
        # We store tuples of (value, minimum_at_this_point)
        self.stack = deque()   

    def push(self, val: int) -> None:
        # If stack is empty, the current val is the minimum.
        # Otherwise, compare val with the minimum of the previous top element.
        if not self.stack:
            current_min = val
        else:
            current_min = min(val, self.stack[-1][1])
            
        self.stack.append((val, current_min))

    def pop(self) -> None:
        # Removes the top tuple from the right side
        self.stack.pop()

    def top(self) -> int:
        # Accesses the value of the top tuple (index -1, first element)
        return self.stack[-1][0]

    def getMin(self) -> int:
        # Accesses the minimum of the top tuple (index -1, second element)
        return self.stack[-1][1]
