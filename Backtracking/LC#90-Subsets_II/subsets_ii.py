# 90. Subsets II
# Difficulty: Medium
# Topics: Array, Backtracking, Bit Manipulation
# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        def backtrack(start, path):
            res.append(path[:])
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        return res

solution_instance = Solution()

case_1_input = [1,2,2]
case_1_output = [[],[1],[1,2],[1,2,2],[2],[2,2]]

case_2_input = [0]
case_2_output = [[],[0]]

assert solution_instance.subsetsWithDup(case_1_input) == case_1_output
assert solution_instance.subsetsWithDup(case_2_input) == case_2_output

print("All tests passed successfully!")