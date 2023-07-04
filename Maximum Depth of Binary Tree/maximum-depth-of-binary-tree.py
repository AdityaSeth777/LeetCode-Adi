class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: if the root is None, the depth is 0
        if root is None:
            return 0
        
        # Recursive case: calculate the depth of the left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # Return the maximum depth of the two subtrees plus one for the root node
        return max(left_depth, right_depth) + 1