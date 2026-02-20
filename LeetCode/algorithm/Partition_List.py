# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        left.next = head
        leftNode, rightNode = left, right
        while leftNode.next:
            if leftNode.next.val >= x:
                rightNode.next = leftNode.next
                rightNode = rightNode.next
                leftNode.next = leftNode.next.next
            else:
                leftNode = leftNode.next
        leftNode.next = right.next
        rightNode.next = None
        return left.next