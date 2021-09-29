# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res=head.val
        ptr = head.next
        while(ptr):
            res = res * 2 + ptr.val
            ptr = ptr.next
        return res
