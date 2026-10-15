# 17. Letter Combinations of a Phone Number
# Difficulty: Medium
# Topics: Hash Table, String, Backtracking
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        digit_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        res = []

        # start = index
        def backtrack(start, path):
            if start == len(digits):
                res.append("".join(path))
                return
            
            actual_digit = digits[start]
            if actual_digit in digit_map:
                for letter in digit_map[actual_digit]:
                    path.append(letter)
                    backtrack(start+1, path)
                    path.pop()

        backtrack(0, [])
        return res

solution_instance = Solution()

case_1_input = "23"
case_1_output = ["ad","ae","af","bd","be","bf","cd","ce","cf"]

case_2_input = "2"
case_2_output = ["a","b","c"]

assert solution_instance.letterCombinations(case_1_input) == case_1_output
assert solution_instance.letterCombinations(case_2_input) == case_2_output

print("All tests passed successfully!")