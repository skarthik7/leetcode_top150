class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1]*len(ratings)
        n = len(ratings)
        for i in range(1,n):
            if ratings[i-1]<ratings[i]:
                candies[i]=candies[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i+1]<ratings[i] and candies[i]<=candies[i+1]:
                candies[i]=max(candies[i+1]+1,candies[i])
            
        return sum(candies)
        #return 47
