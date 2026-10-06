from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = deque()
        
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
                print(stack)
            else:
                temp = 'x'
                if len(stack)>0:
                    temp = stack.pop()

                print("c: ",c,"temp: ",temp)
                if (c == '}' and temp!= '{'):
                    print(' } false')
                    return False
                elif (c == ']' and temp!= '['):
                    return False
                elif (c == ')' and temp!= '('):
                    return False
        print('after for')
        if(len(stack)>0): return False
        return True