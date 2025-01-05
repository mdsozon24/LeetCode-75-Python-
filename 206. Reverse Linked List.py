# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        crr = head
        p = None
        while crr:
            n = crr.next
            crr.next = p
            p = crr
            crr = n
        return p