# TIme Complexity: O(logn)
# Space COmplexity: O(1)
# Approach: Perform infix traversal and always send the previous value to the next node. 
#			There will be at max 2 times when the previous is lesser than node's value.
#			At the first time store both previous and node. Second time replace th node's value with new node's value. Replace value of both nodes.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
            
    def __init__(self):
        self.node1 = None
        self.node2 = None
        
    def assignNodeResult(self, node1, node2):
        if self.node1 is None:
            self.node1 = node1
            self.node2 = node2
        else:
            self.node2 = node2
            
    def infixSearch(self, node, previous):
        if node is None:
            return None
        
        left = self.infixSearch(node.left, previous)
        if left is not None:
            previous = left
            
        if previous is not None and previous.val > node.val:
            self.assignNodeResult(previous, node)
            
        right = self.infixSearch(node.right, node)
        if right is not None:
            return right
        return node
        
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        self.infixSearch(root, None)
        val = self.node1.val
        self.node1.val = self.node2.val
        self.node2.val = val
        return
