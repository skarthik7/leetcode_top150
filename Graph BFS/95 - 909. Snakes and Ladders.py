class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def get(s):
            quot, rem = divmod(s-1, n)
            row = n - 1 - quot
            col = rem if row % 2 != n % 2 else n - 1 - rem
            return row, col

        visited = set()
        queue = [(1, 0)]  # (square, moves)
        while queue:
            s, moves = queue.pop(0)
            if s == n*n:
                return moves
            for next_s in range(s+1, min(s+6, n*n) + 1):
                r, c = get(next_s)
                if board[r][c] != -1:
                    next_s = board[r][c]
                if next_s not in visited:
                    visited.add(next_s)
                    queue.append((next_s, moves + 1))
        return -1