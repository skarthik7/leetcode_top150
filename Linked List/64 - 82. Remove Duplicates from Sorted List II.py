# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        dummy_head.next = head
        prev = dummy_head
        current = head
        while current and current.next:
            if current.val == current.next.val:
                while current and current.next and current.val == current.next.val:
                    current = current.next
                if prev.next == current:
                    prev = prev.next
                else:
                    prev.next = current.next
            else:
                prev = prev.next
            current = current.next
        return dummy_head.next