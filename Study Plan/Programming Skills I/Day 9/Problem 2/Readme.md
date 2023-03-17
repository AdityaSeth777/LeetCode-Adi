Problem -> <https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/?envType=study-plan&id=programming-skills-i>

Explanation:

We create a string alphabet containing all the English lowercase characters.
We initialize an empty string result to store the final result.
We start a while loop with a variable i initialized to 0 to traverse the input string s.
If the current character s[i+2] is a #, we map the substring s[i:i+2] to the corresponding English lowercase character and increment the index i by 3.
Otherwise, we map the current character s[i] to the corresponding English lowercase character and increment the index i by 1.
We append the mapped English lowercase character to the result string result.
Once the while loop completes, we return the final result string result.
