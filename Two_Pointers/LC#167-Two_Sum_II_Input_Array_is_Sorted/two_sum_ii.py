# 167. Two Sum II - Input Array is Sorted
# Difficulty: Medium
# Topics: Array, Two Pointers, Binary Search
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        leftP = 0
        rightP = len(numbers) - 1
        while leftP < rightP:
            if numbers[leftP] + numbers[rightP] == target:
                return [leftP+1, rightP+1]
            elif numbers[leftP] + numbers[rightP] > target:
                # Too big, decrement rightP
                rightP -= 1
            else:
                # Too small, increment leftP
                leftP += 1
                
solution_instance = Solution()

case_1_input = [2,7,11,15]
case_1_target = 9
case_1_output = [1, 2]

case_2_input = [2,3,4]
case_2_target = 6
case_2_output = [1, 3]

case_3_input = [-1,0]
case_3_target = -1
case_3_output = [1, 2]

assert solution_instance.twoSum(case_1_input, case_1_target) == case_1_output
assert solution_instance.twoSum(case_2_input, case_2_target) == case_2_output
assert solution_instance.twoSum(case_3_input, case_3_target) == case_3_output

print("All tests passed successfully!")
