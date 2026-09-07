# 74. Search a 2D Matrix
# Difficulty: Medium
# Topics: Array, Binary Search, Matrix
# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        # find the midpoint in a "flattened" 1D matrix
        # and do normal binary search
        l = 0
        r = rows * cols - 1
        while l <= r:
            mid_idx = (l + r) // 2
            # to get actual matrix repr [row][col] of mid indx
            row_idx_mid = mid_idx // cols
            col_idx_mid = mid_idx % cols
            # normal binary search now
            mid_value = matrix[row_idx_mid][col_idx_mid]
            if target == mid_value:
                return True
            elif target < mid_value:
                r = mid_idx - 1
            else:
                l = mid_idx + 1
        return False

solution_instance = Solution()

case_1_input = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
case_1_target = 3
case_1_output = True

case_2_input = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
case_2_target = 13
case_2_output = False

assert solution_instance.searchMatrix(case_1_input, case_1_target) == case_1_output
assert solution_instance.searchMatrix(case_2_input, case_2_target) == case_2_output

print("All tests passed successfully!")