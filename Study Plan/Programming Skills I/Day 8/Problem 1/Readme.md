Problem -> <https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan&id=programming-skills-i>


Here, we initialize two pointers i and j to 0 and an empty string merged_str to store the merged string. We then loop through both strings word1 and word2 using these pointers and concatenate the ith character of word1 with the jth character of word2 and add it to merged_str. We then increment both pointers by 1.

After the loop, we check if either of the pointers is less than the length of its corresponding string. If so, we concatenate the remaining characters of that string to merged_str.

Finally, we return merged_str as the answer to the problem. This code should correctly merge the two given strings word1 and word2 by adding letters in alternating order while preserving the relative order of the characters.

