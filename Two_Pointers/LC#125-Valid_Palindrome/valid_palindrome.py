# 125. Valid Palindrome
# Difficulty: Easy
# Topics: Two Pointers, String
# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
solution_instance = Solution()

case_1_input = "A man, a plan, a canal: Panama"
case_1_output = True

case_2_input = "race a car"
case_2_output = False

case_3_input = " "
case_3_output = True

assert solution_instance.isPalindrome(case_1_input) == case_1_output
assert solution_instance.isPalindrome(case_2_input) == case_2_output
assert solution_instance.isPalindrome(case_3_input) == case_3_output

print("All tests passed successfully!")