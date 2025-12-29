# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.answer = 0

        def calcZigZag(node: Optional[TreeNode], isLeft: bool, depth: int):
            if not node:
                return

            self.answer = max(self.answer, depth)
            if isLeft:
                calcZigZag(node.right, False, depth + 1)
                calcZigZag(node.left, True, 1)
            else:
                calcZigZag(node.left, True, depth + 1)
                calcZigZag(node.right, False, 1)

        calcZigZag(root, True, 0)
        return self.answer