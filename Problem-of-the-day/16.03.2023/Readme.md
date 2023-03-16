Problem -> <https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/>


The function buildTree takes two input parameters, inorder and postorder, which are the inorder and postorder traversal arrays of the binary tree, respectively. The function returns the root node of the constructed binary tree.

The function first checks if either inorder or postorder is empty. If either of them is empty, it means that there are no nodes left to construct, so the function returns None.

Next, the function finds the root node of the binary tree by getting the last element in the postorder array. It creates a new TreeNode object with the val attribute set to the root node value.

Then, the function finds the index of the root node in the inorder array. This index separates the left subtree nodes from the right subtree nodes in the inorder traversal.

The function recursively constructs the left and right subtrees by calling buildTree with the appropriate subsets of the inorder and postorder arrays.

Finally, the function returns the root node of the constructed binary tree.
