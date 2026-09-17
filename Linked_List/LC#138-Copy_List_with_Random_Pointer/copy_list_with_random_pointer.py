# 138. Copy List with Random Pointer
# Difficulty: Medium
# Topics: Hash Table, Linked List
# https://leetcode.com/problems/copy-list-with-random-pointer/

# Definition for a Node.
from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # map where key = original node and value = deep copy of that original node
        original_to_copy_map = {None: None}

        curr = head
        # first pass just create the copy of the nodes
        while curr:
            copy = Node(curr.val)
            original_to_copy_map[curr] = copy
            curr = curr.next

        # second pass now update the pointers accordingly
        curr = head
        while curr:
            copy_node = original_to_copy_map[curr]

            # find copy_next actual node
            copy_next = curr.next
            copy_next_node = original_to_copy_map[copy_next]
            copy_node.next = copy_next_node

            # find copy_random actual node
            copy_random = curr.random
            copy_random_node = original_to_copy_map[copy_random]
            copy_node.random = copy_random_node

            curr = curr.next

        return original_to_copy_map[head]