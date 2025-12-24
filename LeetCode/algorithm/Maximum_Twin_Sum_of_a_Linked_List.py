# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next

        answer = 0
        for i in range(len(vals) // 2):
            answer = max(answer, vals[i] + vals[-i - 1])
        return answer