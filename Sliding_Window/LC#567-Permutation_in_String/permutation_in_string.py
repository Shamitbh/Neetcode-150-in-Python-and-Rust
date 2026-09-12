# 567. Permutation in String
# Difficulty: Medium
# Topics: Hash Table, Two Pointers, String, Sliding Window
# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l = 0
        freq_count_s1 = [0] * 26
        freq_count_s2 = [0] * 26

        for i in range(len(s1)):
            freq_count_s1[ord(s1[i]) - ord('a')] += 1
            freq_count_s2[ord(s2[i]) - ord('a')] += 1

        if freq_count_s1 == freq_count_s2:
            return True

        for i in range(len(s1), len(s2)):
            # increase s2 freq at index i aka right pointer of window
            freq_count_s2[ord(s2[i]) - ord('a')] += 1
            # decrese s2 freq at index i - len(s1) aka left pointer of window
            freq_count_s2[ord(s2[i - len(s1)]) - ord('a')] -= 1

            if freq_count_s1 == freq_count_s2:
                return True
        return False
    
solution_instance = Solution()

case_1_s1 = "ab"
case_1_s2 = "eidbaooo"
case_1_output = True

case_2_s1 = "ab"
case_2_s2 = "eidboaoo"
case_2_output = False

assert solution_instance.checkInclusion(case_1_s1, case_1_s2) == case_1_output
assert solution_instance.checkInclusion(case_2_s1, case_2_s2) == case_2_output

print("All tests passed successfully!")