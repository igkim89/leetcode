# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    total += node.val
                if low < node.val:
                    stack.append(node.left)
                if high > node.val:
                    stack.append(node.right)
        
        return total
        
        