# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = ListNode()
        odd = ListNode()
        eve = even
        od = odd
        crr = head
        x = 1
        while crr:
            if x%2==0:
                eve.next = crr
                eve = eve.next
            else:
                od.next = crr
                od = od.next
            crr = crr.next
            x+=1

        od.next = even.next
        eve.next = None
        return odd.next
        