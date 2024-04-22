class Solution:
    def reverseWords(self, s: str) -> str:
        k = s.split()
        return " ".join(k[::-1])