# 739. Daily Temperatures
# Difficulty: Medium
# Topics: Array, Stack, Monotonic Stack
# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        # monotonic decreasing stack
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                # calculate answer # of days
                answer[stack_index] = i - stack_index
            # append temp to stack
            stack.append([temp, i])
        return answer

solution_instance = Solution()

case_1_input = [73,74,75,71,69,72,76,73]
case_1_output = [1,1,4,2,1,1,0,0]

case_2_input = [30,40,50,60]
case_2_output = [1,1,1,0]

case_3_input = [30,60,90]
case_3_output = [1, 1, 0]

assert solution_instance.dailyTemperatures(case_1_input) == case_1_output
assert solution_instance.dailyTemperatures(case_2_input) == case_2_output
assert solution_instance.dailyTemperatures(case_3_input) == case_3_output

print("All tests passed successfully!")