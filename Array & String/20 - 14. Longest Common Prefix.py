class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        longestWord=min(strs,key=len)
        for i in range(len(longestWord),-1,-1):
            subString = strs[0][:i]
            for wordIndex in range(1,len(strs)):
                word=strs[wordIndex]
                if subString in word[:i]:
                    count+=1
            if count == len(strs)-1:
                return subString
            else:
                count = 0
        return ""