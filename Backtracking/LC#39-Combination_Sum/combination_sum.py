# 39. Combination Sum
# Difficulty: Medium
# Topics: Array, Backtracking
# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        
        def backtrack(remaining, start, path):
            # base cases
            if remaining == 0:
                res.append(path[:])
                return
            elif remaining < 0:
                return
            
            # backtrack recursively
            for i in range(start, len(candidates)):
                # add this number to the combination path
                path.append(candidates[i])
                # give the current number another chance rather than moving on
                backtrack(remaining - candidates[i], i, path)
                # backtrack by removing the number from the combination to try new ones
                path.pop()

        backtrack(target, 0, [])
        return res

solution_instance = Solution()

case_1_candidates = [2,3,6,7]
case_1_target = 7
case_1_output = [[2,2,3],[7]]

case_2_candidates = [2,3,6,7]
case_2_target = 7
case_2_output = [[2,2,3],[7]]

case_3_candidates = [2]
case_3_target = 1
case_3_output = []

assert solution_instance.combinationSum(case_1_candidates, case_1_target) == case_1_output
assert solution_instance.combinationSum(case_2_candidates, case_2_target) == case_2_output
assert solution_instance.combinationSum(case_3_candidates, case_3_target) == case_3_output

print("All tests passed successfully!")