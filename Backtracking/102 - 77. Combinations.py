class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self._backtrack(1, [], n, k, result)
        return result

    def _backtrack(self, start, curr, n, k, result):
        if len(curr) == k:
            result.append(curr[:])
            return
        for i in range(start, n + 1):
            curr.append(i)
            self._backtrack(i + 1, curr, n, k, result)
            curr.pop()