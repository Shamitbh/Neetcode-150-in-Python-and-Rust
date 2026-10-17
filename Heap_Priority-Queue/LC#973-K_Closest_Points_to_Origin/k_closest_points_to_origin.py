# 973. K Closest Points to Origin
# Difficulty: Medium
# Topics: Array, Math, Divide and Conquer, Geometry, Sorting, Heap (Priority Queue), Quickselect, K-D Tree
# https://leetcode.com/problems/k-closest-points-to-origin/

import heapq
import math
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # max heap of size k so it always evicts max element
        # and we keep k smallest at the end
        max_heap_dists = []
        for x, y in points:
            dist = math.sqrt(x*x + y*y)
            heapq.heappush(max_heap_dists, (-dist, x, y))
            if len(max_heap_dists) > k:
                heapq.heappop(max_heap_dists)
        return [[x, y] for _, x, y in max_heap_dists]

solution_instance = Solution()

case_1_points = [[1,3],[-2,2]]
case_1_k = 1
case_1_output = [[-2,2]]

case_2_points = [[3,3],[5,-1],[-2,4]]
case_2_k = 2
case_2_output = [[-2,4],[3,3]]

assert solution_instance.kClosest(case_1_points, case_1_k) == case_1_output
assert solution_instance.kClosest(case_2_points, case_2_k) == case_2_output

print("All tests passed successfully!")