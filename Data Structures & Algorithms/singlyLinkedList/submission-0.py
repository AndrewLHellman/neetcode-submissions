class ListNode:
    def __init__(self, val: int, next_node=None):
        self.val = val
        self.next_node = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(0)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        cur = self.head
        for _ in range(index+1):
            cur = cur.next_node
            if cur == None:
                return -1
        return cur.val

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val, self.head.next_node)
        if (self.tail == self.head):
            self.tail = new_node
        self.head.next_node = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next_node = new_node
        self.tail = self.tail.next_node

    def remove(self, index: int) -> bool:
        cur = self.head
        for _ in range(index):
            cur = cur.next_node
            if cur == None:
                return False
        if cur.next_node == None:
            return False
        if cur.next_node == self.tail:
            self.tail = cur
        cur.next_node = cur.next_node.next_node
        return True

    def getValues(self) -> List[int]:
        vals = []
        cur = self.head
        while cur.next_node != None:
            cur = cur.next_node
            vals.append(cur.val)
        return vals

        
