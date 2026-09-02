# 49. Group Anagrams
# Difficulty: Medium
# Topics: Array, Hash Table, String, Sorting
# https://leetcode.com/problems/group-anagrams/
import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for word in strs:
            # create charList for this word
            charList = [0] * 26
            # loop through each letter
            for letter in word:
                charList[ord(letter) - ord('a')] += 1
            # Append to result and charList (key) must be hashable (tuple)
            res[tuple(charList)].append(word)
        
        return list(res.values())

solution_instance = Solution()

# Test cases
case_1_input = ["eat","tea","tan","ate","nat","bat"]
case_1_output = [["eat","tea","ate"],["tan","nat"],["bat"]]

case_2_input = [""]
case_2_output = [[""]]

case_3_input = ["a"]
case_3_output = [["a"]]

assert solution_instance.groupAnagrams(case_1_input) == case_1_output
assert solution_instance.groupAnagrams(case_2_input) == case_2_output
assert solution_instance.groupAnagrams(case_3_input) == case_3_output

print("All tests passed successfully!")