from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = deque()
        
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            else:
                temp = 'x'
                if len(stack)>0:
                    temp = stack.pop()

                if (c == '}' and temp!= '{'):
                    return False
                elif (c == ']' and temp!= '['):
                    return False
                elif (c == ')' and temp!= '('):
                    return False        
        return len(stack)==0