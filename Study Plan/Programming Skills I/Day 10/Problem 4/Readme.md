Problem -> <https://leetcode.com/problems/sum-of-left-leaves/description/?envType=study-plan&id=programming-skills-i>


In the sumOfLeftLeaves method, we first check the base case where the root is None. In this case, the sum of left leaves is 0.

For the recursive case, we check if the left child of the current node is a left leaf. If it is, we add its value to the left_leaf_value variable. Otherwise, we set left_leaf_value to 0.

We then recursively calculate the sum of left leaves in the left and right subtrees of the current node. Finally, we return the sum of left leaves in the current subtree, which is the sum of the left_leaf_value, the sum of left leaves in the left subtree, and the sum of left leaves in the right subtree.
