class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self._dfs(board, i, j, word, 0):
                    return True
        return False

    def _dfs(self, board, i, j, word, k):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True
        board[i][j] = '#'
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if self._dfs(board, i + di, j + dj, word, k + 1):
                return True
        board[i][j] = word[k]
        return False