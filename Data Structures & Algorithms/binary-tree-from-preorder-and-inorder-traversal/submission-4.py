# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {}
        for i, elem in enumerate(inorder):
            index_map[elem] = i
        
        def buildTreeWorker(preorder: List[int], inorder: List[int], offset: int = 0) -> Optional[TreeNode]:
            if inorder == []:
                return None
            index = index_map[preorder[0]] - offset
            return TreeNode(inorder[index], buildTreeWorker(preorder[1:index + 1], inorder[:index], offset), buildTreeWorker(preorder[index + 1:], inorder[index+1:], offset + index + 1))
        
        return buildTreeWorker(preorder, inorder)
