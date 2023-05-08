# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        max_depth = 0
        for child in root.children:
            depth = self.maxDepth(child)
            max_depth = max(max_depth, depth)
        
        return max_depth + 1