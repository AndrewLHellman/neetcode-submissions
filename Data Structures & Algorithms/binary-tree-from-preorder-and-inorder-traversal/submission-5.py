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

        self.pre_idx = 0
        
        def buildTreeWorker(left: int, right: int) -> Optional[TreeNode]:
            if left >= right:
                return None

            index = index_map[preorder[self.pre_idx]]
            self.pre_idx += 1
            return TreeNode(inorder[index], buildTreeWorker(left, index), buildTreeWorker(index+1, right))
        
        return buildTreeWorker(0, len(inorder))
