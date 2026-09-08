# 153. Find Minimum in Rotated Sorted Array
# Difficulty: Medium
# Topics: Array, Binary Search
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: list[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                # already sorted
                res = min(res, nums[l])
                return res
            
            # now we know that array was rotated in some way
            mid = (l + r) // 2
            res = min(res, nums[mid])
            # if mid >= l, then real smallest would be in right side
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return res

solution_instance = Solution()

case_1_input = [3,4,5,1,2]
case_1_output = 1

case_2_input = [4,5,6,7,0,1,2]
case_2_output = 0

case_3_input = [11,13,15,17]
case_3_output = 11

assert solution_instance.findMin(case_1_input) == case_1_output
assert solution_instance.findMin(case_2_input) == case_2_output
assert solution_instance.findMin(case_3_input) == case_3_output

print("All tests passed successfully!")