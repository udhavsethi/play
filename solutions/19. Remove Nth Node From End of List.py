# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res, slow, fast = head, head, head
        while fast != None:
            res = slow
            slow = fast
            count=0
            for i in range(n):
                fast = fast.next
                if fast == None:
                    break
                count += 1
        if count < n:
            for j in range(count):
                res = res.next
        if res.next != None:
            res.next = res.next.next
        else:
            # before moving, res was at the element which has to be removed
            # that's also where the head is. so return head.next
            return head.next
        return head
​
