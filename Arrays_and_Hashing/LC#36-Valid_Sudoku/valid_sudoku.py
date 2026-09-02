# 36. Valid Sudoku
# Difficulty: Medium
# Topics: Array, Hash Table, Matrix
# https://leetcode.com/problems/valid-sudoku/

import collections
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                # check for empty position
                if board[r][c] == '.':
                    continue
                # check if this position value already been added to corresponding row, col, or box set
                if (board[r][c] in rows[r] or 
                board[r][c] in cols[c] or 
                board[r][c] in boxes[(r // 3, c // 3)]):
                    # Duplicate found and rules broken
                    return False
                
                # otherwise add this position to 3 sets accordingly
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])
            # print(rows)
            # print(cols)
            # print(boxes)
        # after loop, if haven't returned, then valid soduku board
        return True
            
solution_instance = Solution()

# Test cases
case_1_board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
case_1_output = True

case_2_board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
case_2_output = False

assert solution_instance.isValidSudoku(case_1_board) == case_1_output
assert solution_instance.isValidSudoku(case_2_board) == case_2_output

print("All tests passed successfully!")