# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrderTraversal(root: Optional[TreeNode]) -> List:
            if not root:
                return []
            return inOrderTraversal(root.left) + [root.val] + inOrderTraversal(root.right)
        
        return inOrderTraversal(root)[k-1]