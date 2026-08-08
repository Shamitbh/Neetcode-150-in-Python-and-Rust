# 347. Top K Frequent Elements
# Difficulty: Medium
# Topics: Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect
# https://leetcode.com/problems/top-k-frequent-elements/
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # min heap
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        heap = []
        for num, count in freq_map.items():
            heapq.heappush(heap, [count, num])
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for count, num in heap:
            res.append(num)
        return res

solution_instance = Solution()

# Test cases
case_1_nums = [1,1,1,2,2,3]
case_1_k = 2
case_1_output = [2, 1]

case_2_nums = [1]
case_2_k = 1
case_2_output = [1]

case_3_nums = [1,2,1,2,1,2,3,1,3,2]
case_3_k = 2
case_3_output = [1, 2]

assert solution_instance.topKFrequent(case_1_nums, case_1_k) == case_1_output
assert solution_instance.topKFrequent(case_2_nums, case_2_k) == case_2_output
assert solution_instance.topKFrequent(case_3_nums, case_3_k) == case_3_output

print("All tests passed successfully!")