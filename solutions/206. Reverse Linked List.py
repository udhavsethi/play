# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        elif not head.next.next:
            temp = head.next
            head.next.next = head
            head.next = None
            return temp
​
        first, second, third = head, head.next, head.next.next
        first.next = None
        while third is not None:
            second.next = first
            first = second
            second = third
            third = third.next
        second.next = first
        return second
​
