# 230. Kth Smallest Element in a BST
# Difficulty: Medium
# Topics: Tree, Depth-First Search, Binary Search Tree, Binary Tree
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        arr = []
        def in_order(node):
            if not node:
                return
            in_order(node.left)
            arr.append(node.val)
            in_order(node.right)
        in_order(root)
        return arr[k-1]

        # Time: O(n)
        # Space: O(n)
        # Could be optimized in terms of space
