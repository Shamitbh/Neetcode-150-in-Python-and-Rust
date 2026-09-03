# 150. Evaluate Reversh Polish Notation
# Difficulty: Medium
# Topics: Array, Math, Stack
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        # Algorithm:
        # place each operand onto stack
        # when encountering an operator, pop last 2 elements,
        # do operation, and push back onto stack

        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                second_val = stack.pop()
                first_val = stack.pop()
                
                operation_result = None
                match token:
                    case "+":
                        operation_result = first_val + second_val
                    case "-":
                        operation_result = first_val - second_val
                    case "*":
                        operation_result = first_val * second_val
                    case "/":
                        operation_result = int(first_val / second_val)
                
                stack.append(operation_result)
            else:
                stack.append(int(token))
        return stack[0]
    
solution_instance = Solution()

case_1_input = ["2","1","+","3","*"]
case_1_output = 9

case_2_input = ["4","13","5","/","+"]
case_2_output = 6

case_3_input = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
case_3_output = 22

assert solution_instance.evalRPN(case_1_input) == case_1_output
assert solution_instance.evalRPN(case_2_input) == case_2_output
assert solution_instance.evalRPN(case_3_input) == case_3_output

print("All tests passed successfully!")