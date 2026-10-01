# 102. Binary Tree Level Order Traversal
# Difficulty: Medium
# Topics: Tree, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        levels = []
        if not root:
            return levels
        
        def helper(node, level):
            print(levels)
            if len(levels) == level:
                levels.append([])
            
            levels[level].append(node.val)

            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
            return 
        
        helper(root, 0)
        return levels