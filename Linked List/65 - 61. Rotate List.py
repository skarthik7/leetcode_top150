# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        first = second = head
        length = 0
        while first:
            first = first.next
            length += 1
        k %= length
        first = head
        for _ in range(k):
            first = first.next
        while first.next:
            first = first.next
            second = second.next
        first.next = head
        head = second.next
        second.next = None
        return head