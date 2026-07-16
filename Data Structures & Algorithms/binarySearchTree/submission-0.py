from typing import Self

class TreeNode:
    def __init__(self, key: int, val: int, left: Optional[Self] = None, right: Optional[Self] = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = TreeNode(key, val)

        def dfs(key: int, val: int, root: Optional[TreeNode]) -> TreeNode:
            if not root:
                return TreeNode(key, val)
            if key == root.key:
                root.val = val
            elif key < root.key:
                root.left = dfs(key, val, root.left)
            else:
                root.right = dfs(key, val, root.right)
            return root

        self.root = dfs(key, val, self.root)

    def get(self, key: int) -> int:
        if not self.root:
            return -1
        
        def dfs(key: int, root: Optional[TreeNode]) -> int:
            if not root:
                return -1
            if key == root.key:
                return root.val
            if key < root.key:
                return dfs(key, root.left)
            else:
                return dfs(key, root.right)
        
        return dfs(key, self.root)


    def getMin(self) -> int:
        if not self.root:
            return -1

        curr = self.root
        while curr.left:
            curr = curr.left

        return curr.val

    def getMax(self) -> int:
        if not self.root:
            return -1

        curr = self.root
        while curr.right:
            curr = curr.right

        return curr.val

    def __minNode__(self, root: TreeNode) -> TreeNode:
        curr = root
        while curr.left:
            curr = curr.left
        return curr

    def remove(self, key: int) -> None:
        if not self.root:
            return
        
        def dfs(key: int, root: Optional[TreeNode]) -> Optional[TreeNode]:
            if not root:
                return None

            if key < root.key:
                root.left = dfs(key, root.left)
            elif key > root.key:
                root.right = dfs(key, root.right)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    minNode = self.__minNode__(root.right)
                    root.key = minNode.key
                    root.val = minNode.val
                    root.right = dfs(minNode.key, root.right)
            return root
        
        self.root = dfs(key, self.root)

    def getInorderKeys(self) -> List[int]:        
        def dfs(root: Optional[TreeNode]):
            if not root:
                return []
            return dfs(root.left) + [root.key] + dfs(root.right)

        return dfs(self.root)
