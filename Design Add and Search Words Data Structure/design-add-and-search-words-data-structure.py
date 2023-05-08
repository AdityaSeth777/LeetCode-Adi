class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        def search_in_node(word, node):
            for i, c in enumerate(word):
                if c not in node.children:
                    if c == '.':
                        for child in node.children:
                            if search_in_node(word[i+1:], node.children[child]):
                                return True
                    return False
                else:
                    node = node.children[c]
            return node.is_word

        return search_in_node(word, self.root)