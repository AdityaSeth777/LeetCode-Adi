from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # base case
        if not inorder or not postorder:
            return None

        # find the root node in the postorder traversal array
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # find the index of the root node in the inorder traversal array
        root_idx = inorder.index(root_val)

        # recursively construct the left and right subtrees
        root.left = self.buildTree(inorder[:root_idx], postorder[:root_idx])
        root.right = self.buildTree(
            inorder[root_idx+1:], postorder[root_idx:-1])

        return root
