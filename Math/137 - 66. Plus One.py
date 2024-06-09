class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stringA = ''
        for ele in digits:
            stringA=stringA+str(ele)
        answer = int(stringA) + 1
        return [int(x) for x in str(answer)] 
        #return [int(i) for i in str(string[-1]+1)]
        