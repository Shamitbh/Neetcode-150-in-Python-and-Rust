# 3. Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topics: Hash Table, String, Sliding Window
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicates_set = set()
        length = 0
        l = 0
        if not s:
            return length
        for r in range(len(s)):
            while s[r] in duplicates_set:
                duplicates_set.remove(s[l])
                l += 1
            
            # add to set
            duplicates_set.add(s[r])
            # calc max length
            length = max(length, r - l + 1)
        return length

solution_instance = Solution()

case_1_input = "abcabcbb"
case_1_output = 3

case_2_input = "bbbbb"
case_2_output = 1

case_3_input = "pwwkew"
case_3_output = 3

assert solution_instance.lengthOfLongestSubstring(case_1_input) == case_1_output
assert solution_instance.lengthOfLongestSubstring(case_2_input) == case_2_output
assert solution_instance.lengthOfLongestSubstring(case_3_input) == case_3_output

print("All tests passed successfully!")