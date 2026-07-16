class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if not self.root:
            self.root = newNode
            return

        current = self.root
        while True:
            if key < current.key:
                if current.left == None:
                    current.left = newNode
                    return
                current = current.left
            elif key > current.key:
                if current.right == None:
                    current.right = newNode
                    return
                current = current.right
            else:
                current.val = val
                return

    def get(self, key: int) -> int:
        current = self.root
        while current != None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.val
        return -1


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
