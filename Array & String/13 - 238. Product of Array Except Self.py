class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=[1]*n
        
        for i in range(0, n-1): 
            left[i+1] = left[i]*nums[i]
        
        
        for i in range(0, n-1):
            left[-1 - i] *= left[0]
            left[0] *= nums[-1 - i]
            
        return left