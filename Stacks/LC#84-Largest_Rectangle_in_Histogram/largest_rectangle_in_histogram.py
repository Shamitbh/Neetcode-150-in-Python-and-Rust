# 84. Largest Rectangle in Histogram
# Difficulty: Hard
# Topics: Array, Stack, Monotonic Stack, Range Minimum/Maximum Query
# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        if len(heights) == 1:
            return heights[0]
        max_area = 0
        stack = [] # [index of potential start, height]

        # start with 1st height
        stack.append([0, heights[0]])

        for i in range(1, len(heights)):
            indx_popped, height_popped = None, None
            while stack and heights[i] < stack[-1][1]:
                # calculate area
                width = i - stack[-1][0]
                height = stack[-1][1]
                area = width * height
                max_area = max(area, max_area)
                indx_popped, height_popped = stack.pop()
            if indx_popped is not None:
                stack.append([indx_popped, heights[i]])
            else:
                stack.append([i, heights[i]])

        for i, h in stack:
            max_area = max(h * (len(heights) - i), max_area)
        
        return max_area

solution_instance = Solution()

case_1_input = [2,1,5,6,2,3]
case_1_output = 10

case_2_input = [2,4]
case_2_output = 4

assert solution_instance.largestRectangleArea(case_1_input) == case_1_output
assert solution_instance.largestRectangleArea(case_2_input) == case_2_output

print("All tests passed successfully!")