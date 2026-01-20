# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None
        while node:
            if prev:
                node.val, prev.val = prev.val, node.val
                prev = None
            else:
                prev = node
            node = node.next
        return head