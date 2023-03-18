Problem -> <https://leetcode.com/problems/valid-anagram/description/?envType=study-plan&id=programming-skills-i>

In this implementation, we first check if the length of s and t are equal. If they are not, they cannot be anagrams, so we return False.

Then, we create a dictionary freq to count the frequency of characters in s. We iterate over each character in s and update its count in the dictionary.

Next, we iterate over each character in t and check if it is present in the dictionary freq and if its count is greater than 0. If it is not present or its count is 0, t cannot be an anagram of s, so we return False. Otherwise, we decrement its count in the dictionary.

If we have iterated over all characters in t and none of them have failed the above check, we return True, indicating that t is an anagram of s.
