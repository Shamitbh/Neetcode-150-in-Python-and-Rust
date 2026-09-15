# 239. Sliding Window Maximum
# Difficulty: Hard
# Topics: Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue, Range Minimum/Maximum Query
# https://leetcode.com/problems/sliding-window-maximum/

import heapq
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # max heap (value, index)
        heap = []
        result = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            # check if we go over window size
            if i >= k - 1:
                # remove the max element of heap
                # if the index was out of bounds on left
                # in the window
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                result.append(-heap[0][0])
        return result

solution_instance = Solution()

case_1_nums = [1,3,-1,-3,5,3,6,7]
case_1_k = 3
case_1_output = [3,3,5,5,6,7]

case_2_nums = [1]
case_2_k = 1
case_2_output = [1]

assert solution_instance.maxSlidingWindow(case_1_nums, case_1_k) == case_1_output
assert solution_instance.maxSlidingWindow(case_2_nums, case_2_k) == case_2_output

print("All tests passed successfully!")