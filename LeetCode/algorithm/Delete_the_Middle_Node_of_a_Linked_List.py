# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1

        if n <= 1:
            return None

        cur = head
        for _ in range(n // 2 - 1):
            cur = cur.next

        cur.next = cur.next.next
        return head