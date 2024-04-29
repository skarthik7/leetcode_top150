class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for ele in s:
            if ele.isalpha() or ele.isnumeric():
                newStr+=ele.lower()
        
        return newStr==newStr[::-1]