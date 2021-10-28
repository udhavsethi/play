# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def areIdentical(self, leftnode, rightnode):
        if leftnode is None and rightnode is None:
            return True
        elif leftnode is None:
            return False
        elif rightnode is None:
            return False
        return (
            leftnode.val == rightnode.val
            and self.areIdentical(leftnode.left, rightnode.right)
            and self.areIdentical(leftnode.right, rightnode.left)
        )
​
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.areIdentical(root.left, root.right)
