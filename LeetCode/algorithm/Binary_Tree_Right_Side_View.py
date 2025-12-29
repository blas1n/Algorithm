from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        answer = []
        queue = deque([root])
        
        while queue:
            tmp = []
            view = None
            while queue:
                node = queue.popleft()
                view = node.val
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue.extend(tmp)
            if view != None:
                answer.append(view)
        return answer