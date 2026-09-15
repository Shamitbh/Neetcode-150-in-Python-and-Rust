# 21. Merge Two Sorted lists
# Difficulty: Easy
# Topics: Linked List, Recursion
# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = curr = ListNode()

        while list1 and list2:
            # check which list has smaller value and that becomes
            # curr's next value
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            # update curr
            curr = curr.next
            
        # check if one of the lists ended early
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        
        return dummy.next