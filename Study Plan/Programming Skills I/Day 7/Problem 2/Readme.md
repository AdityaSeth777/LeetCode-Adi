Problem -> <https://leetcode.com/problems/reshape-the-matrix/description/?envType=study-plan&id=programming-skills-i>

Here, we first compute the number of rows m and columns n of the given matrix mat. We then check if the reshape operation is possible by verifying that the product of m and n is equal to the product of the new number of rows r and the new number of columns c. If the reshape operation is not possible, we return the original matrix mat.

If the reshape operation is possible, we create a flattened version of the matrix mat using a list comprehension that iterates over each row and each element within each row. We then initialize an empty list reshaped_mat to store the reshaped matrix.

We loop through each row of the new matrix and slice the flattened matrix to extract c elements at a time, starting from the i*cth index and ending at the (i+1)*cth index, where i is the current row index. We then append the sliced row to reshaped_mat.

Finally, we return the reshaped_mat as the answer to the problem. This code should correctly reshape the given matrix mat into a new one with the specified number of rows r and columns c while preserving the original data order if the reshape operation is possible.
