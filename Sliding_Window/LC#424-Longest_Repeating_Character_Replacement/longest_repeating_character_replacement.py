# 424. Longest Repeating Character Replacement
# Difficulty: Medium
# Topics: Hash Table, String, Sliding Window
# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        max_freq = 0
        l = 0
        result = 0
        for r in range(len(s)):
            # choose character s[r], add to freq_map
            # if window_size - most_freq
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            max_freq = max(max_freq, freq_map[s[r]])

            # shrink if window size - max_freq of character
            # would be bigger than k
            while (r - l + 1) - max_freq > k:
                freq_map[s[l]] -= 1
                l += 1
            
            # result is max of result or window_size
            result = max(result, r - l + 1)
        return result
        
solution_instance = Solution()

case_1_s = "ABAB"
case_1_k = 2
case_1_output = 4

case_2_s = "AABABBA"
case_2_k = 1
case_2_output = 4

assert solution_instance.characterReplacement(case_1_s, case_1_k) == case_1_output
assert solution_instance.characterReplacement(case_2_s, case_2_k) == case_2_output

print("All tests passed successfully!")
