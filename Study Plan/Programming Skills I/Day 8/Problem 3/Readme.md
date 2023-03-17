Problem -> <https://leetcode.com/problems/find-the-difference/description/?envType=study-plan&id=programming-skills-i>


The findTheDifference function takes two string inputs s and t, and returns the extra character that was added to t.

The function first initializes two dictionaries s_freq and t_freq to keep track of the frequency of each character in s and t, respectively. It then counts the frequency of each character in s and t using a for loop and the get method of dictionaries.

Finally, the function compares the frequencies of each character in t to the frequencies in s to find the extra character. It does this by iterating over the characters in t using another for loop, and checking if each character is not in s_freq or if the frequency of the character in t_freq is not the same as the frequency in s_freq. When it finds a character that meets one of these conditions, it returns that character as the extra character that was added to t.
