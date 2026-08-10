# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        p = head
        nodes = []
        while p:
            nodes.append(p.val)
            p = p.next
        
        n = len(nodes)
        max_sum = 0
        for i in range(0, n//2):
            max_sum = max(max_sum, nodes[i] + nodes[n-i-1])

        return max_sum
