# 78. Subsets
# Difficulty: Medium
# Topics: Array, Backtracking, Bit Manipulation
# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        def dfs(index, path):
            if index == len(nums):
                res.append(path[:])
                return
            # decision 1: use number
            path.append(nums[index])
            dfs(index + 1, path)
            # pop that choice
            path.pop()

            # decision 2: don't use number
            dfs(index + 1, path)

        dfs(0, [])
        return res
    
solution_instance = Solution()

case_1_input = [1,2,3]
case_1_output = solution_instance.subsets(case_1_input)
case_1_output_sorted = sorted(case_1_output, key=len)
case_1_expected = [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]

case_2_input = [0]
case_2_output = solution_instance.subsets(case_2_input)
case_2_output_sorted = sorted(case_2_output, key=len)
case_2_expected = [[],[0]]

assert case_1_output_sorted == case_1_expected
assert case_2_output_sorted == case_2_expected

print("All tests passed successfully!")