# TIme Complexity: O(n)
# Space Complexity: O(1)
# Approach: Perform inorder traversal. 
#			If both node's left and right exist, connect left node's next to right node
# 			If node's right and node's next exists, connect node's right to node's next left


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def inordertraversal(self, node):
        if node is None:
            return
        
        if node.right is not None:
            node.left.next = node.right
        if node.right is not None and node.next is not None:
            node.right.next = node.next.left
            
        self.inordertraversal(node.left)
        self.inordertraversal(node.right)
        
    def connect(self, root: 'Node') -> 'Node':
        self.inordertraversal(root)
        return root
        