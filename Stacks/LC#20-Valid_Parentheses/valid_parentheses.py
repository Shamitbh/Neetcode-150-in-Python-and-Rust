# 20. Valid Parentheses
# Difficulty: Easy
# Topics: String, Stack, Bracket Sequences
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        paren_dict = {')': '(', ']': '[', '}':'{'}
        stack = []
        # loop through string
        for ch in s:
            # if close, check top of stack and if same, pop
            if ch in paren_dict:
                if stack and stack[-1] == paren_dict[ch]:
                    stack.pop()
                else:
                    return False
            else:
                # if open parentheses, add to stack
                stack.append(ch)
        
        return not stack

solution_instance = Solution()

case_1_input = "()"
case_1_output = True

case_2_input = "()[]{}"
case_2_output = True

case_3_input = "(]"
case_3_output = False

case_4_input = "([])"
case_4_output = True

case_5_input = "([)]"
case_5_output = False


assert solution_instance.isValid(case_1_input) == case_1_output
assert solution_instance.isValid(case_2_input) == case_2_output
assert solution_instance.isValid(case_3_input) == case_3_output
assert solution_instance.isValid(case_4_input) == case_4_output
assert solution_instance.isValid(case_5_input) == case_5_output

print("All tests passed successfully!")