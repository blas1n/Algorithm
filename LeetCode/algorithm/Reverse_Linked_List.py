class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        cur = head
        while cur:
            next = nodes[-1] if nodes else None
            new = ListNode(cur.val, next)
            nodes.append(new)
            cur = cur.next

        return nodes[-1] if nodes else None