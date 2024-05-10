class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap = {}
        for char in magazine:
            if char in hashMap:
                hashMap[char] += 1
            else:
                hashMap[char] = 1
        for char in ransomNote:
            if char in hashMap:
                if hashMap[char] == 0:
                    del hashMap[char]
                    return False
                hashMap[char] -= 1
            else:
                return False
        return True