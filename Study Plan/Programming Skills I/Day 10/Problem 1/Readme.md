Problem -> <https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/?envType=study-plan&id=programming-skills-i>

In the getDecimalValue method, we first initialize a variable decimal_value to 0, which will hold the decimal value of the binary number represented by the linked list.

Then, we traverse the linked list from the head to the tail using a while loop. Inside the loop, we shift the decimal value to the left by one bit (i.e., multiply it by 2) and add the current node's value. This simulates the process of building up the decimal value from the binary digits in the linked list.

Finally, we return the decimal value.
