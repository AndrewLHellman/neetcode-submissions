# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        elif not self.isBalanced(root.left):
            return False
        elif not self.isBalanced(root.right):
            return False
        elif abs(self.getHeight(root.right) - self.getHeight(root.left)) > 1:
            return False
        return True
    
    def getHeight(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1