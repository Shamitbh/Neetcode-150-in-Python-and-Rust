# 235. Lowest Common Ancestor of a Binary Search Tree
# Difficulty: Medium
# Topics: Tree, Depth-First Search, Binary Search Tree, Binary Tree, Binary Lifting, Lowest Common Ancestor
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Recursive approach

        if not root or not p or not q:
            return None
        
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

        # Iterative approach

        # curr = root
        # while curr:
        #     if p.val > curr.val and q.val > curr.val:
        #         # go to right subtree
        #         curr = curr.right
        #     elif p.val < curr.val and q.val < curr.val:
        #         # go to left subtree
        #         curr = curr.left
        #     else:
        #         return curr