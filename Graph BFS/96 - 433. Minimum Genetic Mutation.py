from collections import deque

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        queue = deque([(start, 0)])
        while queue:
            curr, steps = queue.popleft()
            if curr == end:
                return steps
            for i in range(len(curr)):
                for c in 'ACGT':
                    next = curr[:i] + c + curr[i+1:]
                    if next in bank:
                        queue.append((next, steps+1))
                        bank.remove(next)
        return -1