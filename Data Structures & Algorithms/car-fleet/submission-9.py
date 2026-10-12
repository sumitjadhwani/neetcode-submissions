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
        result = 1
        steps = []
        for step in pos_steps.values():
            steps.append(step)
        
        current_max_time = steps[0]
        for i in range(len(steps)):
            if(steps[i] > current_max_time):
                result+=1
                current_max_time = steps[i]
                continue
            else:
                continue
        return result