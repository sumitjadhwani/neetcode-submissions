class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []  # stores the arrival time of each fleet's leader

        # 1. Pair each car's (position, speed) and sort from closest to farthest
        for p, s in sorted(zip(position, speed), reverse=True):
            # 2. Calculate how long this car takes to reach the target alone
            time = (target - p) / s

            # 3. If it's the first car, OR it takes LONGER than the fleet ahead,
            #    it can't catch up -> it becomes the leader of a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)