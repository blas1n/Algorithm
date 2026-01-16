# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = 0
        coef = 1
        while l1 != None:
            a += l1.val * coef
            coef *= 10
            l1 = l1.next

        b = 0
        coef = 1
        while l2 != None:
            b += l2.val * coef
            coef *= 10
            l2 = l2.next

        acc = a + b
        answer = ListNode()
        node = answer
        while acc > 0:
            node.val = acc % 10
            acc //= 10
            if acc > 0:
                next = ListNode()
                node.next = next
                node = next
        return answer