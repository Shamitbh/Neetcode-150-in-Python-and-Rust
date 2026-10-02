# 199. Binary Tree Right Side View
# Difficulty: Medium
# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        
        queue = deque([root])
        result = []
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                curr_node = queue.popleft()
                # only add right most nodes of level to result
                if i == level_size - 1:
                    result.append(curr_node.val)
                # check children of curr node and add to queue
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
        return result
