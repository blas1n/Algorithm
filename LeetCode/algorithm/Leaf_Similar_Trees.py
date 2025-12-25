# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def get_leaf(root: Optional[TreeNode]) -> List[int]:
    leaf = []
    stack = [root]
    visited = set()

    while stack:
        node = stack.pop()
        if not node or node in visited:
            continue

        visited.add(node)

        if node.left or node.right:
            stack.append(node.right)
            stack.append(node.left)
        else:
            leaf.append(node.val)

    return leaf

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return get_leaf(root1) == get_leaf(root2)