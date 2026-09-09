# 33. Search in Rotated Sorted Array
# Difficulty: Medium
# Topics: Array, Binary Search
# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        res = -1
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            # l -> mid is a sorted segment
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # mid -> r is a sorted segment
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        # if not found, return -1
        return -1

solution_instance = Solution()

case_1_input = [4,5,6,7,0,1,2]
case_1_target = 0
case_1_output = 4

case_2_input = [4,5,6,7,0,1,2]
case_2_target = 3
case_2_output = -1

case_3_input = [1]
case_3_target = 0
case_3_output = -1

assert solution_instance.search(case_1_input, case_1_target) == case_1_output
assert solution_instance.search(case_2_input, case_2_target) == case_2_output
assert solution_instance.search(case_3_input, case_3_target) == case_3_output

print("All tests passed successfully!")
