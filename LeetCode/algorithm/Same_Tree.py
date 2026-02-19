# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def preorder(node1, node2):
            if not node1 or not node2:
                return bool(node1) == bool(node2)
            if node1.val != node2.val:
                return False
            if not preorder(node1.left, node2.left):
                return False
            return preorder(node1.right, node2.right)
        return preorder(p, q)