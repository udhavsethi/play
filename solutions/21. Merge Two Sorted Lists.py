# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
​
# recursive
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
​
​
# iterative
# class Solution:
#     def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         if l1 is None:
#             return l2
#         elif l2 is None:
#             return l1
​
#         if l1.val >= l2.val:
#             head, l2 = l2, l2.next
#         else:
#             head, l1 = l1, l1.next
#         headref = head
#         while l1 is not None and l2 is not None:
#             if l1.val >= l2.val:
#                 head.next = l2
#                 l2 = l2.next
#             else:
#                 head.next = l1
#                 l1 = l1.next
#             head = head.next
#         head.next = l2 if l1 is None else l1
#         return headref
            
        
