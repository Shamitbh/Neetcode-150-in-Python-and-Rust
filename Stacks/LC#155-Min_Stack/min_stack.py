# 155. Min Stack
# Difficulty: Medium
# Topics: Stack, Design
# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.min_stack:
            min_val = min(value, self.min_stack[-1])
            self.min_stack.append(min_val)
        else:
            self.min_stack.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

solution_instance = MinStack()

case_1_input_commands = ["MinStack","push","push","push","getMin","pop","top","getMin"]
case_1_input = [[],[-2],[0],[-3],[],[],[],[]]
case_1_output = [None,None,None,None,-3,None,0,-2]

solution_instance.push(-2)
solution_instance.push(0)
solution_instance.push(-3)
assert solution_instance.getMin() == -3
solution_instance.pop()
assert solution_instance.top() == 0
assert solution_instance.getMin() == -2

print("All tests passed successfully!")