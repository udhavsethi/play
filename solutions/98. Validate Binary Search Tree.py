# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxValue(self, root):
        if not root.left and not root.right:
            return root.val
        elif not root.left:
            return max(root.val, self.maxValue(root.right))
        elif not root.right:
            return max(root.val, self.maxValue(root.left))
        else:
            return max(root.val, self.maxValue(root.left), self.maxValue(root.right))
    
    def minValue(self, root):
        if not root.left and not root.right:
            return root.val
        elif not root.left:
            return min(root.val, self.minValue(root.right))
        elif not root.right:
            return min(root.val, self.minValue(root.left))
        else:
            return min(root.val, self.minValue(root.left), self.minValue(root.right))
​
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None or (not root.left and not root.right):
            return True
        elif not root.left:
            return (self.minValue(root.right) > root.val) and self.isValidBST(root.right)
        elif not root.right:
            return (self.maxValue(root.left) < root.val) and self.isValidBST(root.left)
        else:
            return (
                (self.maxValue(root.left) < root.val)
                and (self.minValue(root.right) > root.val)
                and self.isValidBST(root.left)
                and self.isValidBST(root.right)
