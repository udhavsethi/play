# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
​
# cleaner recursive solution
class Solution:
    def reverse(self, node, prev):
        if prev is None:
            return node
        newhead = self.reverse(prev, prev.next)
        prev.next = node
        return newhead
​
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        return self.reverse(None, head)
​
​
# recursive solution
# class Solution:
#     def reverse(self, node):
#         if node.next is None:
#             return node
#         prev = self.reverse(node.next)
#         prev.next = node
#         return node
​
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
