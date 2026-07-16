# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def _merge(self, list_a: List[Optional[ListNode]], list_b: List[Optional[ListNode]]):
        cur_a, cur_b = list_a, list_b
        head = ListNode()
        cur = head
        while cur_a and cur_b:
            if cur_a.val <= cur_b.val:
                cur.next = cur_a
                cur_a = cur_a.next
                cur = cur.next
                cur.next = None
            else:
                cur.next = cur_b
                cur_b = cur_b.next
                cur = cur.next
                cur.next = None
        if cur_a:
            cur.next = cur_a
        if cur_b:
            cur.next = cur_b
        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self._merge(lists[0], lists[1])
        else:
            m = len(lists) // 2
            return self._merge(self.mergeKLists(lists[:m]), self.mergeKLists(lists[m:]))