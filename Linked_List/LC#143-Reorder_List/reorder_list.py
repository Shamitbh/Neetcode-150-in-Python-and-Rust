# 143. Reorder List
# Difficulty: Medium
# Topics: Linked List, Two Pointers, Stack, Recursion
# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # get middle of list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # now we have slow which is start of 2nd half of list
        # now reverse 2nd half
        dummy = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = dummy
            dummy = curr
            curr = temp
        # now we have dummy which is 1st element of 2nd half of reversed list

        # now we have to just re-order list
        first = head
        second = dummy
        while second.next:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
        