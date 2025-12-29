# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def delete_node(node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not node:
        return node
    
    if key < node.val:
        node.left = delete_node(node.left, key)
    elif key > node.val:
        node.right = delete_node(node.right, key)
    else:
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        
        min_node = find_min(node.right)
        node.val = min_node.val
        node.right = delete_node(node.right, min_node.val)
    return node

def find_min(node):
    while node.left:
        node = node.left
    return node

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return delete_node(root, key)