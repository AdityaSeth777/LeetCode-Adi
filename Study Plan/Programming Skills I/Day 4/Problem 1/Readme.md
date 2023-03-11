Problem -> https://leetcode.com/problems/sign-of-the-product-of-an-array/submissions/913107986/


The arraySign function takes an array nums of integers as input and returns the sign of the product of all the values in the array.

The function initializes the variable product to 1 and then iterates over each value in the nums array, multiplying it with the product variable. The resulting product represents the product of all values in the nums array.

The function then calls the signFunc function, passing the product as an argument, to determine the sign of the product. The signFunc function returns 1 if the product is positive, -1 if the product is negative, and 0 if the product is 0.

Finally, the arraySign function returns the sign of the product.