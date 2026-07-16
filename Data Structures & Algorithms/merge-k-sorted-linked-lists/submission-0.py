# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        size = 0
        final_size = 0
        for l in lists:
            while l:
                l = l.next
                final_size += 1
        while final_size != size:
            min_val = float("inf")
            min_index = -1
            for i, l in enumerate(lists):
                if l and l.val < min_val:
                    min_val = l.val
                    min_index = i
            cur.next = lists[min_index]
            lists[min_index] = lists[min_index].next
            cur = cur.next
            cur.next = None
            size += 1
    
        return head.next

            