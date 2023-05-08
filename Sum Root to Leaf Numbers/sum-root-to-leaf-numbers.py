class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Define a helper function to recursively traverse the tree and compute the sum
        def traverse(node, path_sum):
            if not node:
                return 0
            path_sum = path_sum * 10 + node.val
            if not node.left and not node.right:  # Leaf node
                return path_sum
            left_sum = traverse(node.left, path_sum)
            right_sum = traverse(node.right, path_sum)
            return left_sum + right_sum
        
        # Call the helper function on the root node
        return traverse(root, 0)