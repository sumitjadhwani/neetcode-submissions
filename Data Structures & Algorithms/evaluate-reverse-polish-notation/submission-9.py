import operator
from collections import deque

# 1. Define the mapping dictionary
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        if len(tokens) == 1:
            return int(tokens[0])
        result = 1
        for token in tokens:
            if token not in ('+', '-', '*', '/'):
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token in ops:
                    result = int(ops[token](a, b))
                stack.append(result)
        return result

                