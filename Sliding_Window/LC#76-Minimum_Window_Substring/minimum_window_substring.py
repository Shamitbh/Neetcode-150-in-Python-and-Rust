# 76. Minimum Window Substring
# Difficulty: Hard
# Topics: Hash Table, String, Sliding Window
# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = {}, {}

        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)

        have, need = 0, len(countT)
        l = 0
        res, resLen = [-1, -1], float('inf')
        for r in range(len(s)):
            # add s[r] to window map
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                # satisfied that specific character condition
                have += 1
            
            # check valid window
            # while valid, store result (min)
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                # check if character at left pointer no longer satisfies condition
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                # increment left pointer
                l += 1
        # Finally use res pointers and return the actual string
        left, right = res
        return s[left:right + 1] if resLen != float('inf') else ""

solution_instance = Solution()

case_1_s = "ADOBECODEBANC"
case_1_t = "ABC"
case_1_output = "BANC"

case_2_s = "a"
case_2_t = "a"
case_2_output = "a"

case_3_s = "a"
case_3_t = "aa"
case_3_output = ""

assert solution_instance.minWindow(case_1_s, case_1_t) == case_1_output
assert solution_instance.minWindow(case_2_s, case_2_t) == case_2_output
assert solution_instance.minWindow(case_3_s, case_3_t) == case_3_output

print("All tests passed successfully!")