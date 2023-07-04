class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Base case: if the root is None, the sum is 0
        if root is None:
            return 0
        
        # Recursive case: check if the left child is a left leaf and add its value to the sum
        if root.left is not None and root.left.left is None and root.left.right is None:
            left_leaf_value = root.left.val
        else:
            left_leaf_value = 0
        
        # Recursively calculate the sum of left leaves in the left and right subtrees
        left_sum = self.sumOfLeftLeaves(root.left)
        right_sum = self.sumOfLeftLeaves(root.right)
        
        # Return the sum of left leaves in the current subtree
        return left_leaf_value + left_sum + right_sum