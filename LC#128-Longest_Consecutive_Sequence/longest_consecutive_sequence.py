# 128. Longest Consecutive Sequence
# Difficulty: Medium
# Topics: Array, Hash Table, Union-Find
# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # use set to store numbers
        sequence_set = set()
        for num in nums:
            sequence_set.add(num)
        
        max_length_of_sequence = 0
        # iterate through, if num - 1 in set, then part of sequence
        for num in sequence_set:
            if num - 1 not in sequence_set:
                # this number is the start of a sequence then
                i = 0
                while num + i in sequence_set:
                    i += 1
                max_length_of_sequence = max(max_length_of_sequence, i)
        return max_length_of_sequence

solution_instance = Solution()

case_1_input = [100,4,200,1,3,2]
case_1_output = 4

case_2_input = [0,3,7,2,5,8,4,6,0,1]
case_2_output = 9

case_3_input = [1,0,1,2]
case_3_output = 3

assert solution_instance.longestConsecutive(case_1_input) == case_1_output
assert solution_instance.longestConsecutive(case_2_input) == case_2_output
assert solution_instance.longestConsecutive(case_3_input) == case_3_output

print("All tests passed successfully!")