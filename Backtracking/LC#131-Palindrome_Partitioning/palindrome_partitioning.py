# 131. Palindrome Partitioning
# Difficulty: Medium
# Topics: String, Dynamic Programming, Backtracking
# https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []

        def isPalindrome(string_to_check):
            return string_to_check == string_to_check[::-1]

        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return
            
            for end in range(start, len(s)):
                substring = s[start:end+1]

                if isPalindrome(substring):
                    # add substring to path
                    path.append(substring)
                    # backtrack
                    backtrack(end + 1, path)
                    # pop
                    path.pop()

        backtrack(0, [])
        return res

solution_instance = Solution()

case_1_input = "aab"
case_1_output = [["a","a","b"],["aa","b"]]

case_2_input = "a"
case_2_output =[["a"]]

assert solution_instance.partition(case_1_input) == case_1_output
assert solution_instance.partition(case_2_input) == case_2_output

print("All tests passed successfully!")