# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        queue=[root]
        res = []
        while len(queue) != 0:
            thislevel = []
            children = []
            while len(queue) != 0:
                el = queue.pop(0)
                thislevel.append(el.val)
                el.left and children.append(el.left)
                el.right and children.append(el.right)
            res.append(thislevel)
            for child in children:
                queue.append(child)
        return res
