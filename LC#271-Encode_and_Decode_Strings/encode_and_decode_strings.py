# 271. Encode and Decode Strings
# Difficulty: Medium
# Topics: Array, String, Design
# https://leetcode.com/problems/encode-and-decode-strings/

from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        output = ""
        for word in strs:
            output += str(len(word)) + "#" + word
        
        return output
    
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = []
        i = 0
        while i < len(s):
            j = i
            
            while s[j] != "#":
                j += 1

            # now we hit the delimeter
            word_len = int(s[i:j])
            start_word_indx = j + 1
            end_word_indx = start_word_indx + word_len
            word = s[start_word_indx:end_word_indx]
            result.append(word)

            i = end_word_indx
        return result
            
solution_instance = Solution()

# Test cases
case_1 = ["Hello","World"]
encoded_1 = solution_instance.encode(case_1)
decoded_1 = solution_instance.decode(encoded_1)

case_2 = [""]
encoded_2 = solution_instance.encode(case_2)
decoded_2 = solution_instance.decode(encoded_2)


assert case_1 == decoded_1
assert case_2 == decoded_2

print("All tests passed successfully!")