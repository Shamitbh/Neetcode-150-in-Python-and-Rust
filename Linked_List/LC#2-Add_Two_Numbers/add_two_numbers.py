# 2. Add Two Numbers
# Difficulty: Medium
# Topics: Linked List, Math, Recursion
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            # calculate sum for 2 curr nodes
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0
            digit_sum = val_1 + val_2 + carry
            carry = digit_sum // 10
            remainder = digit_sum % 10
            curr.next = ListNode(remainder)

            # update pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            curr = curr.next

        return dummy.next
        