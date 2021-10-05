# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
# review
​
# using two pointers
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        try:
            while fast is not None:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True
        except:
            return False
​
# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         visited = set()
#         curr = head
#         while curr is not None:
#             if curr in visited:
#                 return True
#             else:
#                 visited.add(curr)
#             curr = curr.next
#         return False
