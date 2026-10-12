class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pos = {}

        if len(position) == 0: 
            return 0
        elif len(position) == 1:
            return 1
        for i in range(len(position)):
            sorted_pos[position[i]]=(target - position[i])/speed[i]
        
        pos_steps = dict(sorted(sorted_pos.items(),reverse=True))
        # print(pos_steps)
        stack = []
        
        for step in pos_steps.values():
            stack.append(step)

            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
        
