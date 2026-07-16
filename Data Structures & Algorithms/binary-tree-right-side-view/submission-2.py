# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        q = deque()
        q.append(root)

        while q:
            qLen = len(q)
            right = None
            for _ in range(qLen):
                curr = q.popleft()
                if curr:
                    right = curr
                    q.append(curr.left)
                    q.append(curr.right)
            if right:
                result.append(right.val)
        
        return result