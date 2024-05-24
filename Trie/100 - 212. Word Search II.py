class TrieNode:
    def __init__(self):
        self.is_word = False
        self.word = None
        self.children = {}

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = True
            node.word = word

        self.result = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.children:
                    self._dfs(board, i, j, root)
        return self.result

    def _dfs(self, board, i, j, node):
        char = board[i][j]
        node = node.children[char]
        if node.is_word:
            self.result.append(node.word)
            node.is_word = False
        board[i][j] = '#'
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] in node.children:
                self._dfs(board, ni, nj, node)
        board[i][j] = char