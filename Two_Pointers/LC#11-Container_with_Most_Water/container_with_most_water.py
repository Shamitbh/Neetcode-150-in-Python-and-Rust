# 11. Container with Most Water
# Difficulty: Medium
# Topics: Array, Two Pointers, Greedy
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            min_height = min(height[l], height[r])
            width = r - l
            area = min_height * width
            max_area = max(area, max_area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_area

solution_instance = Solution()

case_1_input = [1,8,6,2,5,4,8,3,7]
case_1_output = 49

case_2_input = [1,1]
case_2_output = 1

assert solution_instance.maxArea(case_1_input) == case_1_output
assert solution_instance.maxArea(case_2_input) == case_2_output

print("All tests passed successfully!")