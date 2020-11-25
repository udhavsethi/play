# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def ifInRange(self, val, low, high):
        if val >= low and val <= high:
            return val
        return 0
​
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root.left == None and root.right == None:
            return self.ifInRange(root.val, low, high)
        elif root.left == None:
            return self.ifInRange(root.val, low, high) + self.rangeSumBST(root.right, low, high)
        elif root.right == None:
            return self.ifInRange(root.val, low, high) + self.rangeSumBST(root.left, low, high)
        else:
            return self.ifInRange(root.val, low, high) + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
​
