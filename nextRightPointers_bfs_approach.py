# Time COmplexity: O(n)
# Space Complexity: O(# of leaves)
# Approach: Do a BFS level order traversal and connect each node's next in the level
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
    def connect(self, root: 'Node') -> 'Node':
        queue = [root]
        
        if root is None:
            return root
        
        while len(queue) != 0:
            queueLen = len(queue)
            if queueLen == 1:
                elem = queue.pop(0)
                elem.next = None
                if elem.left is not None:
                    queue.append(elem.left)
                    
                if elem.right is not None:
                    queue.append(elem.right)
            else:
                prev = queue.pop(0)
                if prev.left is not None:
                    queue.append(prev.left)
                    
                if prev.right is not None:
                    queue.append(prev.right)
                    
                for i in range(1, queueLen):
                    nextNode = queue.pop(0)
                    if nextNode.left is not None:
                        queue.append(nextNode.left)
                    
                    if nextNode.right is not None:
                        queue.append(nextNode.right)
                    
                    prev.next = nextNode
                    prev = nextNode
                    
        return root
                    
                
        