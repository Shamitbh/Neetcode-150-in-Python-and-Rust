# 46. Permutations
# Difficulty: Medium
# Topics: Array, Backtracking
# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack(path)
                    path.pop()
        
        backtrack([])
        return res
    
solution_instance = Solution()

case_1_input = [1,2,3]
case_1_output = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

case_2_input = [0,1]
case_2_output = [[0,1],[1,0]]

case_3_input = [1]
case_3_output = [[1]]

assert solution_instance.permute(case_1_input) == case_1_output
assert solution_instance.permute(case_2_input) == case_2_output
assert solution_instance.permute(case_3_input) == case_3_output

print("All tests passed successfully!")