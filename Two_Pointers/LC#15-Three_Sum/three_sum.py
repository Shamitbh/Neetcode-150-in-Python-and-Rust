# 125. Three Sum
# Difficulty: Medium
# Topics: Array, Two Pointers, Sorting
# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result_set = set()
        nums.sort()

        # now do two sum 2
        for i in range(len(nums) - 1):
            l = i + 1
            r = len(nums) - 1
            target = nums[i] * -1
            while l < r:
                if nums[l] + nums[r] == target:
                    result_set.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        result_list = [list(item) for item in result_set]
        return result_list

solution_instance = Solution()

case_1_input = [-1,0,1,2,-1,-4]
case_1_output = [[-1,0,1],[-1,-1,2]]

case_2_input = [0,1,1]
case_2_output = []

case_3_input = [0,0,0]
case_3_output = [[0,0,0]]

assert solution_instance.threeSum(case_1_input) == case_1_output
assert solution_instance.threeSum(case_2_input) == case_2_output
assert solution_instance.threeSum(case_3_input) == case_3_output

print("All tests passed successfully!")