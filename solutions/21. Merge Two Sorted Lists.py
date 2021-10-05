# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
​
        if l1.val >= l2.val:
            head, l2 = l2, l2.next
        else:
            head, l1 = l1, l1.next
        headref = head
        while l1 is not None and l2 is not None:
            if l1.val >= l2.val:
                head.next = l2
                head = head.next
                l2 = l2.next
            else:
                head.next = l1
                head = head.next
                l1 = l1.next
        head.next = l2 if l1 is None else l1
        return headref
            
        
