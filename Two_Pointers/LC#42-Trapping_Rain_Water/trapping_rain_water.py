# 42. Trapping Rain Water
# Difficulty: Hard
# Topics: Array, Two Pointers, Dynamic Programming, Stack Monotonic Stack
# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: list[int]) -> int:
        # # Time Complexity: O(n)
        # # Space Complexity: O(n)
        # max_left_arr = [0] * len(height)
        # max_right_arr = [0] * len(height)

        # max_left = 0
        # for i in range(1, len(height)):
        #     max_left = max(max_left, height[i-1])
        #     max_left_arr[i] = max_left

        # max_right = 0
        # for i in range(len(height) - 2, -1, -1):
        #     max_right = max(max_right, height[i+1])
        #     max_right_arr[i] = max_right

        # max_water_area = 0
        # for i in range(len(height)):
        #     area = min(max_left_arr[i], max_right_arr[i]) - height[i]
        #     if area >= 0:
        #         max_water_area += area
        # return max_water_area

        # Time Complexity: O(n)
        # Space Complexity: O(1)
        l, r = 0, len(height) - 1
        max_l = height[l]
        max_r = height[r]
        max_water_area = 0
        while l < r:
            if height[l] <= height[r]:
                area = min(max_l, max_r) - height[l]
                if area > 0:
                    max_water_area += area
                l += 1
                max_l = max(max_l, height[l])
            else:
                area = min(max_l, max_r) - height[r]
                if area > 0:
                    max_water_area += area
                r -= 1
                max_r = max(max_r, height[r])
        return max_water_area

solution_instance = Solution()

case_1_input = [0,1,0,2,1,0,1,3,2,1,2,1]
case_1_output = 6

case_2_input = [4,2,0,3,2,5]
case_2_output = 9

assert solution_instance.trap(case_1_input) == case_1_output
assert solution_instance.trap(case_2_input) == case_2_output

print("All tests passed successfully!")