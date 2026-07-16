# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder == []:
            return None
        i = 0
        while preorder[i] not in inorder:
            i += 1
        index = inorder.index(preorder[i])
        return TreeNode(inorder[index], self.buildTree(preorder, inorder[:index]), self.buildTree(preorder, inorder[index+1:]))
