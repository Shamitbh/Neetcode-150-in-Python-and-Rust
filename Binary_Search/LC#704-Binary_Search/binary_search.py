# 704. Binary Search
# Difficulty: Easy
# Topics: Array, Binary Search
# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        result = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                result = mid
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return result

solution_instance = Solution()

case_1_input = [-1,0,3,5,9,12]
case_1_target = 9
case_1_output = 4

case_2_input = [-1,0,3,5,9,12]
case_2_target = 2
case_2_output = -1

assert solution_instance.search(case_1_input, case_1_target) == case_1_output
assert solution_instance.search(case_2_input, case_2_target) == case_2_output

print("All tests passed successfully!")