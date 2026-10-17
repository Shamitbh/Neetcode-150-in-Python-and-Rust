# 1046. Last Stone Weight
# Difficulty: Easy
# Topics: Array, Heap (Priority Queue)
# https://leetcode.com/problems/last-stone-weight/

import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # max heap
        stones = [stone * -1 for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            heaviest = heapq.heappop(stones)
            second_heaviest = heapq.heappop(stones)
            if heaviest != second_heaviest:
                new_weight = heaviest - second_heaviest
                heapq.heappush(stones, new_weight)
            
        return -stones[0] if stones else 0

solution_instance = Solution()

case_1_input = [2,7,4,1,8,1]
case_1_output = 1

case_2_input = [1]
case_2_output = 1

assert solution_instance.lastStoneWeight(case_1_input) == case_1_output
assert solution_instance.lastStoneWeight(case_2_input) == case_2_output

print("All tests passed successfully!")