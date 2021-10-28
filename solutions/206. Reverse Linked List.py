# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
# review
# cleaner recursive solution
class Solution:
    def reverse(self, left, right):
        if right is None:
            return left
        newhead = self.reverse(right, right.next)
        right.next = left
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
#         if head is None:
#             return head
#         newhead = head
