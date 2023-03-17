Problem -> <https://leetcode.com/problems/matrix-diagonal-sum/description/?envType=study-plan&id=programming-skills-i>

Here, we first compute the length n of the given matrix mat. We then initialize two variables primary_sum and secondary_sum to 0 to keep track of the sum of elements on the primary and secondary diagonals, respectively.

We then loop through each row of the matrix and add the element in the ith row and ith column to primary_sum, and the element in the ith row and n-i-1th column to secondary_sum. The n-i-1 index is used to traverse the secondary diagonal in the opposite direction of the primary diagonal.

Finally, we need to check if the center element of the matrix is counted twice, once in each diagonal. If the length n of the matrix is odd, then we need to subtract the center element from the secondary_sum. We then return the sum of the primary_sum and secondary_sum as the answer to the problem. This code should correctly compute the sum of the matrix diagonals as specified in the problem.
