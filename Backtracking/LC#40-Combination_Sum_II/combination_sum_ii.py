# 40. Combination Sum II
# Difficulty: Medium
# Topics: Array, Backtracking
# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()

        def backtrack(remaining, start, path):
            if remaining == 0:
                res.append(path[:])
                return
            elif remaining < 0:
                return

            for i in range(start, len(candidates)):
                # since its sorted, return early if element > target
                if candidates[i] > target:
                    return
                # make sure to skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # add this number to the combination path
                path.append(candidates[i])
                # backtrack as we can't use same number again
                backtrack(remaining - candidates[i], i + 1, path)
                # backtrack by removing the number from the combination to try new ones
                path.pop()
            
        backtrack(target, 0, [])
        return res

solution_instance = Solution()

case_1_candidates = [10,1,2,7,6,1,5]
case_1_target = 8
case_1_output = [[1,1,6],[1,2,5],[1,7],[2,6]]

case_2_candidates = [2,5,2,1,2]
case_2_target = 5
case_2_output = [[1,2,2],[5]]

assert solution_instance.combinationSum2(case_1_candidates, case_1_target) == case_1_output
assert solution_instance.combinationSum2(case_2_candidates, case_2_target) == case_2_output

print("All tests passed successfully!")