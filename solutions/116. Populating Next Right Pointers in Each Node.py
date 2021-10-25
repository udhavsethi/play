"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
​
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = []
        if root is not None:
            queue.append(root)
        children = []
        while len(queue) != 0:
            node = queue.pop(0)
            if node.left is not None:
                children.append(node.left)
                children.append(node.right)
​
            while len(queue) != 0:
                node.next = queue.pop(0)
                node = node.next
                if node.left is not None:
                    children.append(node.left)
                    children.append(node.right)
            node.next = None
            for child in children:
                queue.append(child)
            children = []
        return root
