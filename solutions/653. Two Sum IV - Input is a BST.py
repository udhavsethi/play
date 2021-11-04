# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# review
class Solution:
    def inorder(self, root):
        traversal = []
        if root:
            traversal.extend(self.inorder(root.left))
            traversal.append(root.val)
            traversal.extend(self.inorder(root.right))
        return traversal
​
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        inorder_tr = self.inorder(root)
        left, right = 0, len(inorder_tr)-1
        while left < right:
            if inorder_tr[left] + inorder_tr[right] == k:
                return True
            elif inorder_tr[left] + inorder_tr[right] < k:
                left += 1
            else:
                right -= 1
        return False
