Problem -> <https://leetcode.com/problems/sum-root-to-leaf-numbers/submissions/915099191/>


The traverse function is a recursive helper function that takes in a node and a running sum of the path leading to that node. It computes the sum of all root-to-leaf paths in the subtree rooted at the given node by recursively calling itself on the left and right children of the node and summing up the results. The base case is when the node is a leaf, in which case the function returns the sum of the path leading to that leaf.

The sumNumbers function simply calls the traverse function on the root node with an initial path sum of 0 and returns the final result.
