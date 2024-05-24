class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        return self._search_from_node(word, self.root)

    def _search_from_node(self, word: str, node: TrieNode) -> bool:
        if not word:
            return node.is_word
        if word[0] == '.':
            return any(self._search_from_node(word[1:], child_node) for child_node in node.children.values())
        if word[0] in node.children:
            return self._search_from_node(word[1:], node.children[word[0]])
        return False       


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)