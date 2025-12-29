# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_val, answer, idx = root.val, 1, 1
        queue = deque([root])
        
        while queue:
            tmp = []
            level_sum = 0
            while queue:
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue.extend(tmp)
            if max_val < level_sum:
                max_val = level_sum
                answer = idx
            idx += 1
        return answer