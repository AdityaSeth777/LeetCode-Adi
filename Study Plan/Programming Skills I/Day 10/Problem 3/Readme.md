Problem -> <https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan&id=programming-skills-i>


In the maxDepth method, we first check the base case where the root is None. In this case, the depth of the subtree is 0.

For the recursive case, we calculate the depth of the left and right subtrees by calling the maxDepth method recursively on the left and right child nodes. We then take the maximum depth of the two subtrees and add one for the root node to get the depth of the current subtree.

Finally, we return the maximum depth of the two subtrees plus one. If the root is None, the method returns 0.
