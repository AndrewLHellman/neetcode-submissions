# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        head = None
        cur1 = list1
        cur2 = list2
        if cur1.val <= cur2.val:
            head = cur1
            cur1 = cur1.next
        else:
            head = cur2
            cur2 = cur2.next
        head.next = None
        cur = head
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next
                cur = cur.next
                cur.next = None
            else:
                cur.next = cur2
                cur2 = cur2.next
                cur = cur.next
                cur.next = None
        if cur1:
            cur.next = cur1
        if cur2:
            cur.next = cur2
        return head
