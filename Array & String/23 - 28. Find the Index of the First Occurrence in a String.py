class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        len_haystack, len_needle = len(haystack), len(needle)

        for i in range(len_haystack - len_needle + 1):
            if haystack[i:i+len_needle] == needle:
                return i

        return -1