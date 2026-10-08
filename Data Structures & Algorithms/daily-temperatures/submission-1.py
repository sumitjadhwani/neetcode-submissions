class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        prev = temperatures[0]
        res = [0]*len(temperatures)
        stack = []
        stack.append(0)

        for i in range(1, len(temperatures)):
            curr = temperatures[i]

            if curr > prev:
                    while len(stack)>0 and (curr > temperatures[stack[-1]]):
                        i1 = stack.pop()
                        res[i1] = i - i1
            prev = curr
            stack.append(i)
        while len(stack) > 0:
            res[stack.pop()]=0
        return res