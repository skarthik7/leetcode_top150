class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        left = right = missing = 0
        missing = len(t)
        start = length = float('inf')

        while right < len(s):
            if s[right] in need:
                need[s[right]] -= 1
                if need[s[right]] >= 0:
                    missing -= 1
            right += 1

            while missing == 0:
                if right - left < length:
                    start = left
                    length = right - left

                if s[left] in need:
                    need[s[left]] += 1
                    if need[s[left]] > 0:
                        missing += 1
                left += 1

        return "" if length == float('inf') else s[start:start+length]