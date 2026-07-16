# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        next_node = head.next
        cur = head
        last = None
        while next_node:
            cur.next = last
            last = cur
            cur = next_node
            next_node = next_node.next
        cur.next = last
        return cur
