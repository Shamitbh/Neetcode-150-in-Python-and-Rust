# 242. Valid Anagram
# Difficulty: Easy
# Topics: Hash Table, String, Sorting
# https://leetcode.com/problems/valid-anagram/

class Solution:
    def validAnagram(self, s: str, t: str) -> bool:
        char_count = [0] * 26

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            char_count[ord(s[i]) - ord('a')] += 1
            char_count[ord(t[i]) - ord('a')] -= 1
        
        for char_freq in char_count:
            if char_freq != 0:
                return False
        return True
            
solution_instance = Solution()

# Test cases
case_1_s = "anagram"
case_1_t = "nagaram"

case_2_s = "rat"
case_2_t = "car"

assert solution_instance.validAnagram(case_1_s, case_1_t)
assert not solution_instance.validAnagram(case_2_s, case_2_t)

print("All tests passed successfully!")