# 217. Contains Duplicate
# Difficulty: Easy
# Topics: Array, Hash Table, Sorting
# https://leetcode.com/problems/contains-duplicate/
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = set()
        for num in nums:
            if num in uniqueNums:
                return True
            uniqueNums.add(num)
        return False
            
solution_instance = Solution()

# Test cases
case_1 = [1, 2, 3, 1]
case_2 = [1, 2, 3, 4]
case_3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

assert solution_instance.containsDuplicate(case_1)
assert not solution_instance.containsDuplicate(case_2)
assert solution_instance.containsDuplicate(case_3)

print("All tests passed successfully!")