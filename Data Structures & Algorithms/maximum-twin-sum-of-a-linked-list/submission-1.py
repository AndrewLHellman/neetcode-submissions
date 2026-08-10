# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        temp1 = slow
        temp2 = slow.next.next if slow.next else None
        slow = slow.next if slow.next else slow
        slow.next = temp1
        temp1.next = None

        while temp2 != None:
            temp1 = slow
            slow = temp2
            temp2 = temp2.next
            slow.next = temp1
        
        max_sum = 0
        while head and slow:
            max_sum = max(head.val + slow.val, max_sum)
            head = head.next
            slow = slow.next

        return max_sum
