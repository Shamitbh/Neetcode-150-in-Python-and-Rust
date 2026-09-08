# 875. Koko Eating Bananas
# Difficulty: Medium
# Topics: Array, Binary Search
# https://leetcode.com/problems/koko-eating-bananas/
import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Brute force
        # Time Complexity: O(m * n)
        # Space Complexity: O(1)

        # max_amount_in_a_pile = max(piles)
        # for banana_rate in range(1, max_amount_in_a_pile + 1):
        #     num_hours = 0
        #     for pile in piles:
        #         num_hours_to_finish_this_pile = math.ceil(pile / banana_rate)
        #         num_hours += num_hours_to_finish_this_pile
        #     if num_hours <= h:
        #         return banana_rate
        
        # Optimal (Binary Search)
        # Time Complexity: O(n * log m)
        # Space Complexity: O(1)
        max_amount_in_a_pile = max(piles)
        low = 1
        high = max_amount_in_a_pile
        while low <= high:
            num_hours = 0
            mid = (low + high) // 2
            for pile in piles:
                num_hours_to_finish_this_pile = math.ceil(pile / mid)
                num_hours += num_hours_to_finish_this_pile
            if num_hours <= h:
                min_rate = mid
                high = mid - 1
            else:
                low = mid + 1
        return min_rate

solution_instance = Solution()

case_1_piles = [3,6,7,11]
case_1_h = 8
case_1_output = 4

case_2_piles = [30,11,23,4,20]
case_2_h = 5
case_2_output = 30

case_3_piles = [30,11,23,4,20]
case_3_h = 6
case_3_output = 23

assert solution_instance.minEatingSpeed(case_1_piles, case_1_h) == case_1_output
assert solution_instance.minEatingSpeed(case_2_piles, case_2_h) == case_2_output
assert solution_instance.minEatingSpeed(case_3_piles, case_3_h) == case_3_output

print("All tests passed successfully!")