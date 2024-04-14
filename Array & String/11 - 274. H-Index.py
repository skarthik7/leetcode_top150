class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        #citations=citations[::-1]
        for i in range(len(citations)):
            if citations[i]<=i:
                return i
        return len(citations)     

        