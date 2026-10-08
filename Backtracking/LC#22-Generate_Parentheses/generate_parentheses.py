# 22. Generate Parentheses
# Difficulty: Medium
# Topics: String, Dynamic Programming, Backtracking, Bracket Sequences
# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(open_count, close_count, path):
            if len(path) == 2 * n:
                res.append("".join(path))
                return

            # check if we can still add more open parens
            if open_count < n:
                path.append("(")
                backtrack(open_count + 1, close_count, path)
                path.pop()

            # check if we can add more close parens
            if close_count < open_count:
                path.append(")")
                backtrack(open_count, close_count + 1, path)
                path.pop()

        backtrack(0, 0, [])
        return res

solution_instance = Solution()

case_1_input = 3
case_1_output = ["((()))","(()())","(())()","()(())","()()()"]

case_2_input = 1
case_2_output = ["()"]

assert solution_instance.generateParenthesis(case_1_input) == case_1_output
assert solution_instance.generateParenthesis(case_2_input) == case_2_output

print("All tests passed successfully!")