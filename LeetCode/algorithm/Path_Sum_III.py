# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def getSumCnt(node: Optional[TreeNode], targetSum: int, curSum: int, cache: Dict[int, int]) -> int:
    if not node:
        return 0

    curSum += node.val
    count = cache.get(curSum - targetSum, 0)
    
    cache[curSum] = cache.get(curSum, 0) + 1
    count += getSumCnt(node.left, targetSum, curSum, cache)
    count += getSumCnt(node.right, targetSum, curSum, cache)
    cache[curSum] -= 1

    return count

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return getSumCnt(root, targetSum, 0, {0:1})