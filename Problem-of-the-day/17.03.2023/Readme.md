Problem -> <https://leetcode.com/problems/implement-trie-prefix-tree/description/>


This code implements the Trie data structure in Python. The Trie consists of a root node and a collection of TrieNodes that represent each character in the words that are inserted into the Trie.

The TrieNode class has two attributes: a dictionary of children that maps each character in the alphabet to a TrieNode representing the next character in a word, and a boolean is_end_of_word flag that is True if the TrieNode represents the end of a word.

The Trie class has three methods:

The __init__() method initializes the root node of the Trie.

The insert(word: str) method inserts a word into the Trie by iterating over each character in the word, creating a new TrieNode if the character is not already a child of the current node, and moving down the Trie until the end of the word is reached, where the is_end_of_word flag is set to True.

The search(word: str) method searches for a word in the Trie by iterating over each character in the word, checking if the character is a child of the current node, and moving down the Trie until the end of the word is reached. If the end of the word is reached and the is_end_of_word flag is True, the method returns True, indicating that the word is in the Trie. Otherwise, it returns False.

The startsWith(prefix: str) method checks if there is a previously inserted string that has the prefix prefix, by iterating over each character in the prefix, checking if the character is a child of the current node, and moving down the Trie until the end of the prefix is reached. If the end of the prefix is reached and all the characters have corresponding children in the Trie, the method returns True, indicating that there is a word in the Trie that starts with the given prefix. Otherwise, it returns False.
