# 853. Car Fleet
# Difficulty: Medium
# Topics: Array, Stack, Sorting, Monotonic Stack
# https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [[pos, speed] for pos, speed in zip(position, speed)]

        stack = []
        for pos, speed in sorted(pair)[::-1]:
            # add the time it'll take to reach target to stack
            stack.append((target - pos) / speed)
            # check top of stack and see if top 2 times would collide
            # to make a fleet, if so, pop the further position away
            # from target
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

solution_instance = Solution()

case_1_target = 12
case_1_position = [10,8,0,5,3]
case_1_speed = [2,4,1,1,3]
case_1_output = 3

case_2_target = 10
case_2_position = [3]
case_2_speed = [3]
case_2_output = 1

case_3_target = 100
case_3_position = [0,2,4]
case_3_speed = [4,2,1]
case_3_output = 1

assert solution_instance.carFleet(case_1_target, case_1_position, case_1_speed) == case_1_output
assert solution_instance.carFleet(case_2_target, case_2_position, case_2_speed) == case_2_output
assert solution_instance.carFleet(case_3_target, case_3_position, case_3_speed) == case_3_output

print("All tests passed successfully!")