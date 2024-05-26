class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtrack(1, [], n, k, result)
        return result

    def backtrack(self, start, curr, n, k, result):
        if len(curr) == k:
            result.append(curr[:])
            return
        for i in range(start, n + 1):
            curr.append(i)
            self.backtrack(i + 1, curr, n, k, result)
            curr.pop()