class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1, self.head)
        self.head.next = self.tail

    def isEmpty(self) -> bool:
        if self.head.next == self.tail:
            return True
        return False

    def append(self, value: int) -> None:
        self.tail.prev.next = ListNode(value, self.tail.prev, self.tail)
        self.tail.prev = self.tail.prev.next

    def appendleft(self, value: int) -> None:
        self.head.next.prev = ListNode(value, self.head, self.head.next)
        self.head.next = self.head.next.prev

    def pop(self) -> int:
        if self.tail.prev == self.head:
            return -1
        node = self.tail.prev
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        return node.val

    def popleft(self) -> int:
        if self.head.next == self.tail:
            return -1
        node = self.head.next
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return node.val
