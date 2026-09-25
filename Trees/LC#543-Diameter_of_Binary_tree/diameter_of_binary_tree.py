# 543. Diameter of Binary Tree
# Difficulty: Easy
# Topics: Tree, Depth-First Search, Binary Tree, DP on Trees
# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        # helper dfs to return height
        def dfs(curr):
            if not curr:
                return 0
            height_left = dfs(curr.left)
            height_right = dfs(curr.right)
            # max of itself and current_diameter (left_height + right_height)
            self.diameter = max(self.diameter, height_left + height_right)
            
            # this dfs still returns max height of subtrees under curr node
            return 1 + max(height_left, height_right)

        # run dfs on root
        dfs(root)
        return self.diameter