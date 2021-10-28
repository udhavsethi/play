# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
# recursive solution
class Solution:
    def reverse(self, node):
        if node.next is None:
            return node
        prev = self.reverse(node.next)
        prev.next = node
        return node
​
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        newhead = head
        while newhead.next is not None:
            newhead = newhead.next
        self.reverse(head)
        head.next = None
        return newhead
​
​
​
# iterative solution
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head
#         elif not head.next.next:
#             temp = head.next
#             head.next.next = head
#             head.next = None
#             return temp
​
#         first, second, third = head, head.next, head.next.next
#         first.next = None
#         while third is not None:
#             second.next = first
#             first = second
#             second = third
