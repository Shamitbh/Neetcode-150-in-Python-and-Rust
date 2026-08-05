# 1. Two Sum
# Difficulty: Easy
# Topics: Junior, Array, Hash Table
# https://leetcode.com/problems/two-sum/description/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in indexMap:  
                return [i, indexMap[difference]]
            indexMap[num] = i
            
solution_instance = Solution()

# Test cases
case_1_nums = [2, 7, 11, 15]
case_1_target = 9

case_2_nums = [3, 2, 4]
case_2_target = 6

case_3_nums = [3, 3]
case_3_target = 6

assert solution_instance.twoSum(case_1_nums, case_1_target) == [1, 0]
assert solution_instance.twoSum(case_2_nums, case_2_target) == [2, 1]
assert solution_instance.twoSum(case_3_nums, case_3_target) == [1, 0]

print("All tests passed successfully!")