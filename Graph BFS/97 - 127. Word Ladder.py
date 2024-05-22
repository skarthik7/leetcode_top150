from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        queue = deque([(beginWord, 1)])
        while queue:
            curr, steps = queue.popleft()
            if curr == endWord:
                return steps
            for i in range(len(curr)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next = curr[:i] + c + curr[i+1:]
                    if next in wordSet:
                        queue.append((next, steps+1))
                        wordSet.remove(next)
        return 0