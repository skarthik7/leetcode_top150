# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head, x):
        before = before_node = ListNode(0)
        after = after_node = ListNode(0)
        while head:
            if head.val < x:
                before_node.next = head
                before_node = before_node.next
            else:
                after_node.next = head
                after_node = after_node.next
            head = head.next
        after_node.next = None
        before_node.next = after.next
        return before.next