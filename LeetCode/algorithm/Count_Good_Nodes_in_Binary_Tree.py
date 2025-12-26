# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def getGoodNodes(node: Optional[TreeNode], max_parent: int):
    if not node:
        return 0

    my_value = 0
    if node.val >= max_parent:
        max_parent = node.val
        my_value = 1

    return my_value + getGoodNodes(node.left, max_parent) + getGoodNodes(node.right, max_parent)

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return getGoodNodes(root, -10 ** 4 - 1)