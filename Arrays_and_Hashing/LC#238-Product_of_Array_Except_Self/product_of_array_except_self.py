# 238. Product of Array Except Self
# Difficulty: Medium
# Topics: Array, Prefix Sum
# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        ans = []
        
        # Example
        # nums = [1, 2, 3, 4]
        # left = [1, 1, 2, 6]
        # right= [24, 12, 4, 1]
        left[0] = 1
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]

        right[len(nums)-1] = 1
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        for i in range(len(nums)):
            ans.append(left[i] * right[i])
        
        return ans
            
solution_instance = Solution()

# Test cases
case_1_input = [1, 2, 3, 4]
case_1_output = [24, 12, 8, 6]

case_2_input = [-1,1,0,-3,3]
case_2_output = [0,0,9,0,0]

assert solution_instance.productExceptSelf(case_1_input) == case_1_output
assert solution_instance.productExceptSelf(case_2_input) == case_2_output

print("All tests passed successfully!")