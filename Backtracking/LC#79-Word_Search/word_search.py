# 79. Word Search
# Difficulty: Medium
# Topics: Array, String, Backtracking, Depth-First Search, Matrix
# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        # ensure cells are unique by using set
        path = set()
        def backtrack(r, c, i):
            # base case
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path):
                return False

            path.add((r, c))
            dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            for dr, dc in dirs:
                if backtrack(r+dr, c+dc, i+1):
                    return True
            
            path.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
        return False

solution_instance = Solution()

case_1_board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
case_1_word = "ABCCED"

case_2_board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
case_2_word = "SEE"

case_3_board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
case_3_word = "ABCB"

assert solution_instance.exist(case_1_board, case_1_word)
assert solution_instance.exist(case_2_board, case_2_word)
assert not solution_instance.exist(case_3_board, case_3_word)

print("All tests passed successfully!")