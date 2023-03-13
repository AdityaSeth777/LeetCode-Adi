Problem -> <https://leetcode.com/problems/symmetric-tree/submissions/914458806/>



The isSymmetric function checks if the root is None and returns True if it is. Otherwise, it calls the isMirror function with the left and right subtrees of the root. The isMirror function checks if both nodes are None and returns True if they are. If only one node is None, it returns False. If the values of the nodes are not equal, it returns False. Otherwise, it recursively calls isMirror with the left subtree of the left node and the right subtree of the right node, and with the right subtree of the left node and the left subtree of the right node. If both recursive calls return True, it returns True. Otherwise, it returns False.

The time complexity of this algorithm is O(n), where n is the number of nodes in the binary tree. This is because the algorithm visits each node once. The space complexity is O(h), where h is the height of the binary tree. This is because the algorithm uses a recursive approach, and the maximum depth of the recursive call stack is equal to the height of the binary tree.
