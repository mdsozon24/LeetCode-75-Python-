# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        dam1 = head
        dam2 = head
        pre = None
        while dam2 and dam2.next:
            pre = dam1
            dam1 = dam1.next
            dam2 = dam2.next.next
        pre.next = pre.next.next
        return head