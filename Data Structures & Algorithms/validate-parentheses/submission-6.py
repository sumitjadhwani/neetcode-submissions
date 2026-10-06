class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Map closing brackets to their matching opening brackets
        pairs = {')': '(', '}': '{', ']': '['}
        
        for c in s:
            if c in pairs: # If it's a closing bracket
                # If stack is empty, or the top of stack doesn't match, it's invalid
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop() # It's a match, remove it from the stack
            else: # If it's an opening bracket
                stack.append(c)
                
        # If stack is empty at the end, all brackets were matched
        return len(stack) == 0