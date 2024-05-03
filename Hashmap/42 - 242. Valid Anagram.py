class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for char_s, char_t in zip(s, t):
            count[char_s] = count.get(char_s, 0) + 1
            count[char_t] = count.get(char_t, 0) - 1

        for value in count.values():
            if value != 0:
                return False

        return True